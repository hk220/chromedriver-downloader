import logging
import re
import sys
import urllib.request
import urllib.error

logging.basicConfig(level=logging.DEBUG)

LATEST_RELEASE_URL = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_"
CHROME_DRIVER_URL = "https://chromedriver.storage.googleapis.com/{version}/chromedriver_{arch}.zip"


class ChromeVersionFormatExepction(Exception):
    pass


class Chrome(object):
    def __init__(self, chrome_version: str) -> None:
        self._chrome_version = chrome_version
        
    @property
    def version(self) -> str:
        return self._chrome_version
        
    @property
    def major_version(self) -> str:
        splited_version = self._chrome_version.split('.')
        if len(splited_version) != 4:
            raise ChromeVersionFormatExepction("Must be 4 numbers.")
        
        return '.'.join(splited_version[:-1])
    
    @classmethod
    def parse(cls, version_text: str) -> 'Chrome':
        # google-chrome --version
        # Google Chrome 111.0.5563.64
        if version_text.startswith("Google Chrome"):
            splited_text = version_text.strip().split()
            if len(splited_text) != 3:
                raise ChromeVersionFormatExepction(f"Must be able to divide into 3 words: {version_text}")
            return cls(splited_text[2])
        # dpkg-deb -f ./google-chrome-stable_current_amd64.deb version
        # 111.0.5563.64-1
        if re.match(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\-[0-9]+$", version_text.strip()):
            splited_text = version_text.strip().split("-")
            if len(splited_text) != 2:
                raise ChromeVersionFormatExepction(f"Must be able to divide into 2 words: {version_text}")
            return cls(splited_text[0])
        # 111.0.5563.64
        if re.match(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", version_text.strip()):
            return cls(version_text.strip())
        else:
            raise ChromeVersionFormatExepction(f"Not found format: {version_text}")            


class ChromeDriver(object):
    @staticmethod
    def download(version: str) -> None:
        splited_version = version.split('.')
        if len(splited_version) != 4:
            raise ChromeVersionFormatExepction("Must be 4 numbers.")
        major_version = '.'.join(splited_version[:-1])
        latest_release_url = LATEST_RELEASE_URL + major_version
        body = ""
        try:
            with urllib.request.urlopen(latest_release_url) as res:
                body = res.read()
        except urllib.error.URLError as e:
            logging.critical(f"Fetch chromedriver version error: {e}")
            exit(255)
        chromedriver_version = body.decode("utf-8").strip()
        logging.info(f"chromedriver version: {chromedriver_version}")
        chrome_driver_url = CHROME_DRIVER_URL.format(version=chromedriver_version, arch="linux64")
        try:
            with urllib.request.urlopen(chrome_driver_url) as res:
                data = res.read()
                with open("chromedriver.zip", "wb") as f:
                    f.write(data)
        except urllib.error.URLError as e:
            logging.critical(f"Fetch chromedriver error: {e}")
            exit(255)


def main() -> None:
    # read from stdin
    version_text = "".join(sys.stdin.readlines())
    logging.info(f"version_text: {version_text.strip()}")
    chrome = Chrome.parse(version_text)
    logging.info(f"chrome version: {chrome.version}")
    ChromeDriver.download(chrome.version)

if __name__ == "__main__":
    main()
