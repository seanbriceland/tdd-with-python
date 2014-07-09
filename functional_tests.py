from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)
    
    def tearDown(self):
        self.browser.quit()
    
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
        table = self.browser.find_element_by_id()
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        
        # verify there is an input again to add an item
        # user enters another to-do item
        self.fail('Finish the test!')
        
        # page updates again, showing both items in list
        
        # User wonders if the site will remember the to-do list
        # they take note of the URL 
        
        # visit the url and check to-do list is still there
        
        # All tests run
        browser.quit()
    
if __name__ == '__main__':
    unittest.main(warnings='ignore')