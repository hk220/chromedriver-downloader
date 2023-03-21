import subprocess
import urllib.request

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
    with urllib.request.urlopen(req) as res:
        body = res.read()
    return body.decode("utf-8")

def fetch_chromedriver(version: str) -> None:
    url = CHROME_DRIVER_URL.format(version=version, arch="linux64")
    with urllib.request.urlopen(url) as res:
        data = res.read()
        with open("chromedriver.zip", "wb") as f:
            f.write(data)

def get_chrome_version() -> str:
    output = subprocess.run(['google-chrome', '--version'], capture_output=True, text=True).stdout
    return output

def main() -> None:
    chrome_version = get_chrome_version()
    version = parse_chrome_version(chrome_version)
    major_version = get_major_version(version)
    chromedriver_version = fetch_chromedriver_version(major_version)
    fetch_chromedriver(chromedriver_version)
    
if __name__ == "__main__":
    main()
