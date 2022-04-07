from inspect import classify_class_attrs
import unittest

from src import app
from src.utils import fetch, process

#######################################################
#                       Tests                         #
#######################################################

class UtilsTestsFetch(unittest.TestCase):
    "Tests functions contained in Utils.fetch"
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
        """Tests thats when passed a link the respnse contains intended information"""
        link = "https://en.wikipedia.org/wiki/Wiki"
        response = fetch.get_page(link)
        self.assertIn("Ward Cunningham", response.text)

    def test_strip_page(self):
        """Tests that link, meta, and script tags are stripped from the loaded page"""
        link = "https://en.wikipedia.org/wiki/Dog"
        response = fetch.get_page(link)
        stripped = fetch.strip_page(response.text)
        # print(stripped)
        self.assertNotIn("<link>",stripped)
        self.assertNotIn("<meta>",stripped)
        self.assertNotIn("<script>",stripped)

    def test_fetch_page_nolink(self):
        """Tests that provided a term a wikipedia page will appear"""
        term = "banana"
        expected = "https://en.wikipedia.org/wiki/banana"
        self.assertEqual(fetch.get_page_no_link(term),expected)

    def test_check_if_link(self):
        """Tests that a provided text is a link"""
        term1 = "dog"
        term2 = "https://en.wikipedia.org/wiki/Dog"
        self.assertFalse(fetch.check_if_link(term1))
        self.assertTrue(fetch.check_if_link(term2))

class UtilsTestProcess(unittest.TestCase):
    """Tests Functions contained in Utils.Process"""
    def setUp(self) -> None:
        """Executed prior to each test"""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False
        self.app = app.test_client()

    def test_refrence_format():
        """Tests that the function format_refrences returns properly formatted refrences list."""
        pass
