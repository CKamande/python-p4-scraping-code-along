from lib.scraper import Scraper
from bs4 import BeautifulSoup
import pytest

class Test_Scraper:
    def test_get_page(self):
        "uses Beautiful Soup to get the HTML from a web page"
        scraper = Scraper()
        doc = scraper.get_page()
        assert isinstance(doc, BeautifulSoup)

    def test_get_courses(self):
        "Test get_courses"
        scraper = Scraper()
        course_offerings = scraper.get_courses()
        assert isinstance(course_offerings, list)

    def test_make_courses(self):
        "Test self.courses"
        scraper = Scraper()
        courses = scraper.make_courses()
        assert isinstance(courses, list)
        if courses:
            assert "title" in courses[0]
            assert "description" in courses[0]
