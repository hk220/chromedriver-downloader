from setuptools import setup

setup(
    name="chromedriver downloader",
    version="0.1.0",
    description="This is a tool that estimates the available chromedriver version from the Google Chrome version and downloads chromedriver.zip.",
    author="Kazuki Hara",
    author_email="kazuki.hara.dw3@gmail.com",
    license="MIT",
    url="https://github.com/hk220/chromedriver-downloader",
    entry_points={
        'console_scripts': [
            'chromedriver-downloader = chromedriver_downloader:main'
        ]
    }
)
