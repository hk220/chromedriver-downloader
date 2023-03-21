# Chromedriver Downloader

これは、Google Chromeのバージョンから利用可能なchromedriverのバージョンを推定して、chromedriver.zipをダウンロードするツールです。

現時点では、Linuxかつgoogle chrome専用です。
chromiumまたは、Linux以外の環境では動きません。

This is a tool that estimates the available chromedriver version from the Google Chrome version and downloads chromedriver.zip.

At this time, it is only for Linux and google chrome.
It does not work on chromium or non-Linux environments.

## 使い方 / Usage

```bash
python3 ./chromedriver_downloader.py
```

カレントディレクトリに`chromedriver.zip`がダウンロードされます。

The `chromedriver.zip` will be downloaded to the current directory.
