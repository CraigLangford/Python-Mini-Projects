import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class NewVisitorTest(StaticLiveServerTestCase):
    """
    These functional tests check whether a user can easily navigate around
    the website.
    """

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

        self.assertEqual(1, 2)
        # After a long day of headaches and trying to remember all his friend's
        # phonenumbers, Sam heard about a great phonebook website. He decides
        # to to to check out the websites homepage
        self.browser.get(self.live_server_url)

        # He notices that the title says it's a phonebook
        self.assertIn("phonebook", self.browser.title)

        # He's not to sure what the site is for but he sees there's an "about"
        # section at the top of the page
        about_section = self.browser.find_element_by_id("id_about")
        self.assertEqual(about_section.text, "About")

        # He clicks on it to see what it's all about
        about_section.click()

        # Once the page loads he see's it was designed by Craig Langford to
        # fulfil a hackajob challenge. 
        time.sleep(0.2)
        self.assertIn(
            "Craig Langford",
            self.browser.find_element_by_id("id_about_description").text
        )

        # It also links to the template that Craig used to create the site.
        cookiecutter_link = self.browser.find_element_by_id(
            "id_cookiecutter_link")
        
        # He checks out the template
        cookiecutter_link.click()
        time.sleep(3)
        self.assertEqual(
            self.browser.current_url,
            "https://github.com/pydanny/cookiecutter-django"
        )

        # Looks like it is a project used for django
        self.assertIn("cookiecutter-django",
                      self.browser.find_element_by_tag_name('body').text)
        self.browser.back()

        # Upon returning to the site he also sees that Craig has the source
        # code on his GitHub
        time.sleep(3)
        github_link = self.browser.find_element_by_id(
            "id_github_link")
        github_link.click()
        time.sleep(3)
        self.assertEqual(
            self.browser.current_url,
            "https://github.com/CraigLangford/Python-Mini-Projects/tree/master/Phone-Book/phonebook_project")

        # Looks like it's labelled as his phonebook_project
        self.assertIn("phonebook_project",
                      self.browser.find_element_by_tag_name('body').text)
        self.browser.back()
        time.sleep(3)

        # Project looks good! Time to go back to Home and check it out
        home_section = self.browser.find_element_by_id("id_home")
        self.assertEqual(home_section.text, "Home")
        home_section.click()

        # Looks like he's back at the home page
        time.sleep(0.5)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Phonebook", header_text)

    def test_can_use_phonebook(self):
        """ This tests whether user can create new entries in the phonebook,
        view entries, as well as update and delete them. """

        # Sally is wanting to use an online phonebook and goes to her fabourite
        # site!
        self.browser.get(self.live_server_url)

        # She notices that the title says it's a phonebook
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn("Phonebook", header_text)

        # She sees the phonebook is currently empty, however, there is a button
        # asking her to enter a contact.
        self.assertEqual(1,2, "FUNCTIONAL TEST ONLY COMPLETED TO OPENING PAGE!")
        # Entering the info a pop-up comes up with a form asking for first
        # name, last name and phonenumber

        # Entering all the info she enters her first contact

        # She clicks on the "add contact" button

        # Back at the page she sees her new contact is now in the table

        # She decides to enter a few more contacts. She forgot the last name of
        # one of them so she just enters their first name.

        # She sees her contact entered just with their first name

        # She repeats, however, she forgot the first name of the contact

        # Again she enters a contact with just a phone number

        # Finally she enters a contact with no info

        # The screen alerts her she needs to enter the contact's information
        # still

        # Back at the home page she sees an edit button for the contacts
        # Clicking on it the contact's form pops filled with the previous
        # information

        # She edits the information and submits it. Back at the home page she
        # sees the contact info changed accordingly

        # Finally she wants to delete a contact. Clicking on one of the
        # contacts leads to a pop-up asking her to confirm the deletion to
        # which she confirms

        # The contact is now not in the table

        # Happy with her new phonebook she leaves the browser 

