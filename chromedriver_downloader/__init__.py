import logging
import re
import sys
import urllib.request
import urllib.error
import json

VERSION_API = "https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json"

logging.basicConfig(level=logging.DEBUG)

def download(url, filename):
    try:
        with urllib.request.urlopen(url) as res:
            data = res.read()
            with open(filename, "wb") as f:
                f.write(data)
    except urllib.error.URLError as e:
        logging.critical(f"Fetch {filename} error: {e}")
        exit(255)

def get_url(chrome_version, platform):
    chrome_url = ""
    chromedriver_url = ""
    body = ""
    try:
        with urllib.request.urlopen(VERSION_API) as f:
            body = f.read().decode("utf-8")
    except urllib.error.URLError as e:
        logging.critical(f"Fetch chromedriver version error: {e}")
        exit(255)
    obj = json.loads(body)
    chrome_url = ""
    chromedriver_url = ""
    for v in obj["versions"]:
        if v["version"] == chrome_version:
            for d in v["downloads"]["chrome"]:
                if d["platform"] == platform:
                    chrome_url = d["url"]
            for d in v["downloads"]["chromedriver"]:
                if d["platform"] == platform:
                    chromedriver_url = d["url"]
    return (chrome_url, chromedriver_url)

def main():
    chrome_version = sys.argv[1]
    platform = sys.argv[2]
    chrome_url, chromedriver_url = get_url(chrome_version, platform)
    download(chrome_url, f"chrome-{platform}.zip")
    download(chromedriver_url, f"chromedriver-{platform}.zip")

if __name__ == "__main__":
    main()
