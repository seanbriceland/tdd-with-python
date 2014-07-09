from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)
    

    def tearDown(self):
        self.browser.quit()


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        # go to homepage
        self.browser.get('http://localhost:8000')
        
        # verify title of homepage
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        # verify user input is available for new to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        
        # verify user can enter a to-do item
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        # verify page is updated and lists to-do item
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # verify there is an input again to add an item
        # user enters another to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        # page updates again, showing both items in list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('Use peacock feathers to make a fly')

        # User wonders if the site will remember the to-do list
        # they take note of the URL 
        self.fail('Finish the test!')

        # visit the url and check to-do list is still there
        
        # All tests run
        browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')