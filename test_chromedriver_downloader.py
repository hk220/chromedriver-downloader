import unittest

from chromedriver_downloader import ChromeVersion

class TestChromeVersion(unittest.TestCase):
    
    def test_parse_with_google_chrome_version(self):
        cv = ChromeVersion.parse("Google Chrome 111.0.5563.64\n\n")
        expect = "111.0.5563.64"
        actual = cv.version
        self.assertEqual(actual, expect)

    def test_parse_with_deb_version(self):
        cv = ChromeVersion.parse("111.0.5563.64-1\n")
        expect = "111.0.5563.64"
        actual = cv.version
        self.assertEqual(actual, expect)
        
    def test_parse(self):
        cv = ChromeVersion.parse("111.0.5563.64\n")
        expect = "111.0.5563.64"
        actual = cv.version
        self.assertEqual(actual, expect)

    def test_major_version(self):
        cv = ChromeVersion.parse("111.0.5563.64\n")
        expect = "111.0.5563"
        actual = cv.major_version
        self.assertEqual(actual, expect)
