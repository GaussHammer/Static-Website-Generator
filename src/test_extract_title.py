from extract_title import *
import unittest

class TestExtractTitle(unittest.TestCase):
    def test_title(self):
        title = extract_title("# Hello")
        self.assertEqual(title, "Hello")
    
    def test_exception(self):
        with self.assertRaises(Exception):
            extract_title("Hello")
         