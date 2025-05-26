# lib/Scraper.py

import requests
from bs4 import BeautifulSoup
from lib.Course import Course  # Adjust if the import path differs


class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        """
        Fetches the HTML page content and parses it using BeautifulSoup.
        """
        try:
            url = "http://learn-co-curriculum.github.io/site-for-scraping/courses"
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for bad HTTP status
            doc = BeautifulSoup(response.text, 'html.parser')
            return doc
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def get_courses(self):
        """
        Selects all course elements from the parsed HTML.
        """
        page = self.get_page()
        return page.select('.post') if page else []

    def make_courses(self):
        """
        Extracts title, date, and description for each course and instantiates a Course.
        """
        for course in self.get_courses():
            title = course.select_one("h2").text.strip() if course.select_one("h2") else 'No Title'
            date = course.select_one(".date").text.strip() if course.select_one(".date") else 'No Date'
            description = course.select_one("p").text.strip() if course.select_one("p") else 'No Description'

            new_course = Course(title, schedule=date, description=description)
            self.courses.append(new_course)

        return self.courses

    def print_courses(self):
        """
        Prints all course details to the console.
        """
        for course in self.make_courses():
            print(course)
