# Chromedriver Downloader

これは、標準入力に与えられたGoogle Chromeのバージョンから、利用可能なchromedriverのバージョンを推定して、chromedriver.zipをダウンロードするツールです。

現時点では、google chrome専用です。 たぶん、chromiumでは動きません。

This is a tool that estimates the available chromedriver version from the Google Chrome version given in the standard input and downloads the chromedriver.zip.

At this time, it is only for google chrome.
It may not work on chromium.

## インストール / Install

```
pip install git+https://github.com/hk220/chromedriver-downloader.git
```

## 使い方 / Usage

```bash
# from google-chrome --version
google-chrome --version | chromedriver-downloader
# from deb file
dpkg-deb -f ./google-chrome-stable_current_amd64.deb version | chromedriver-downloader
# from version
echo "111.0.5563.64-1" | chromedriver-downloader
```

カレントディレクトリに`chromedriver.zip`がダウンロードされます。

The `chromedriver.zip` will be downloaded to the current directory.

## テスト / Test

```
# unitest
make test
# docker test
docker build .
```
