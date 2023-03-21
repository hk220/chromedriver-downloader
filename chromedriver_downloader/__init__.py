import logging
import subprocess
import urllib.request
import urllib.error

logging.basicConfig(level=logging.DEBUG)

LATEST_RELEASE_URL = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_"
CHROME_DRIVER_URL = "https://chromedriver.storage.googleapis.com/{version}/chromedriver_{arch}.zip"

class ChromeVersionFormatExepction(Exception):
    pass

def parse_chrome_version(text: str) -> str:
    splited_text = text.strip().split()
    if len(splited_text) != 3:
        raise ChromeVersionFormatExepction(f"Must be able to divide into 3 words: {text}")
    
    version = splited_text[2]
    return version

def get_major_version(version: str) -> str:
    splited_version = version.split('.')
    if len(splited_version) != 4:
        raise ChromeVersionFormatExepction("Must be 4 numbers.")
    
    return '.'.join(splited_version[:-1])

def fetch_chromedriver_version(major_version: str) -> str:
    url = LATEST_RELEASE_URL + major_version
    req = urllib.request.Request(url)
    body = ""
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
    except urllib.error.URLError as e:
        logging.critical(f"Fetch chromedriver version error: {e}")
        exit(255)
    return body.decode("utf-8")

def fetch_chromedriver(version: str) -> None:
    url = CHROME_DRIVER_URL.format(version=version, arch="linux64")
    try:
        with urllib.request.urlopen(url) as res:
            data = res.read()
            with open("chromedriver.zip", "wb") as f:
                f.write(data)
    except urllib.error.URLError as e:
        logging.critical(f"Fetch chromedriver error: {e}")
        exit(255)

def get_chrome_version() -> str:
    output = subprocess.run(['google-chrome', '--version'], capture_output=True, text=True).stdout
    return output

def main() -> None:
    chrome_version = get_chrome_version()
    logging.info(f"google-chrome --version: {chrome_version.strip()}")
    version = parse_chrome_version(chrome_version)
    logging.info(f"chrome version: {version}")
    major_version = get_major_version(version)
    chromedriver_version = fetch_chromedriver_version(major_version)
    logging.info(f"chromedriver version: {chromedriver_version}")
    fetch_chromedriver(chromedriver_version)
    
if __name__ == "__main__":
    main()
