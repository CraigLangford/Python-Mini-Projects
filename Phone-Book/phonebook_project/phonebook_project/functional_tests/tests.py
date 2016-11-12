from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        """ Load the website and wait 3 seconds for it to load. """
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """ Close the session once the tests are finished. """
        self.browser.quit()

    def test_can_open_website_and_read_about_section(self):
        """ This tests whether user can read the "about section" when visiting
        new website """

        # After a long day of headaches and trying to remember all his friend's
        # phonenumbers, Sam heard about a great phonebook website. He decides
        # to to to check out the websites homepage
        self.browser.get(self.live_server_url)

        # He notices that the title says it's a phonebook
        self.assertIn("phonebook", self.browser.title)

        # He's not to sure what the site is for but he sees there's an "avout"
        # section at the top of the page
        about_section = self.browser.find_element_by_id("id_about")
        self.assertEqual(about_section.text, "About")

        # He clicks on it to see what it's all about
        about_section.click()

        # Once the page loads he see's it was designed by Craig Langford to
        # fulfil a hackajob challenge. Furthermore, it links to the template
        # that Craig used to create the site as well as the source code on
        # Craig's GitHub
        time.sleep(0.2)
        self.assertIn(
            "Craig Langford",
            self.browser.find_element_by_id("id_about_description").text
        )
        cookiecutter_link = self.browser.find_element_by_id(
            "id_cookiecutter_link")
        cookiecutter_link.click()
        time.sleep(3)
        self.assertEqual(
            self.browser.current_url,
            "https://github.com/pydanny/cookiecutter-django"
        )
        self.assertIn("cookiecutter-django",
                      self.browser.find_element_by_tag_name('body').text)
        self.browser.back()
        time.sleep(3)
        github_link = self.browser.find_element_by_id(
            "id_github_link")
        github_link.click()
        time.sleep(3)
        self.assertEqual(
            self.browser.current_url,
            "https://"
        )
