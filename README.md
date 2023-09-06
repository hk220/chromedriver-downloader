# Chromedriver Downloader

これは、引数に与えられたバージョンのchrome.zipとchromedriver.zipをダウンロードするツールです。

現時点では、google chrome専用です。 chromiumでは動きません。

## インストール / Install

```
pip install git+https://github.com/hk220/chromedriver-downloader.git
```

## 使い方 / Usage

```bash
chromedriver-downloader "115.0.5763.0" linux64
```

カレントディレクトリに`chrome-<platform>.zip`と`chromedriver-<platform>.zip`がダウンロードされます。
