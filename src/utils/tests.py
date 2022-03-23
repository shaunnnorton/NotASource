from multiprocessing.sharedctypes import Value
from re import T
import unittest

from src import app
from src.utils import fetch

#######################################################
#                       Tests                         #
#######################################################

class UtilsTests(unittest.TestCase):
    "Tests functions contained in Utils"
    def setUp(self) -> None:
        """Executed prior to each test"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()

    def test_real_link_invalid(self):
        """Tests that an invalid wikipedia link retruns False."""
        link = "https://en.wikipedia.org/wiki/Dgae"
        response = fetch.test_link(link)
        print(response)
        self.assertFalse(response[0])

    def test_real_link_valid(self):
        """Tests that a valid wikipedia link returns True."""
        link = "https://en.wikipedia.org/wiki/Dog"
        response = fetch.test_link(link)
        print(response)
        self.assertTrue(response[0])

    def test_fetch_page(self):
        link = "https://en.wikipedia.org/wiki/Wiki"
        response = fetch.get_page(link)
        self.assertIn("Ward Cunningham", response)