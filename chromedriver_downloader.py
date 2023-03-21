import logging
import urllib.request

LATEST_RELEASE_URL = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_"
CHROME_DRIVER_URL = "https://chromedriver.storage.googleapis.com/{version}/chromedriver_{arch}.zip"

class ChromeVersionFormatExepction(Exception):
    pass

def get_chrome_version(text: str) -> str:
    splited_text = text.strip().split()
    if len(splited_text) != 3:
        raise ChromeVersionFormatExepction("Must be able to divide into 3 words.")
    
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
    urllib.request.urlretrieve(url=url, filename="chromedriver.zip")
