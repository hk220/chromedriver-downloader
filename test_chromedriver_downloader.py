import unittest

from chromedriver_downloader import get_chrome_version, get_major_version

class TestChromeDriverDownloader(unittest.TestCase):

    def test_get_chrome_version(self):
        text = "Google Chrome 111.0.5563.64\n"
        expect = "111.0.5563.64"
        actual = get_chrome_version(text)
        self.assertEqual(actual, expect)

    def test_get_major_version(self):
        version = "111.0.5563.64"
        expect = "111.0.5563"
        actual = get_major_version(version)
        self.assertEqual(actual, expect)
