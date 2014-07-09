from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(1)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retreive_it_later(self):
        # go to homepage
        self.browser.get('http://localhost:8000')
        
        # verify title of homepage
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')
        
        # verify user can enter a to-do item
        
        # verify user input is available for new to-do item
        
        # verify page is updated and lists to-do item
        
        # verify there is an input again to add an item
        # user enters another to-do item
        
        # page updates again, showing both items in list
        
        # User wonders if the site will remember the to-do list
        # they take note of the URL 
        
        # visit the url and check to-do list is still there
        
        # All tests run
        browser.quit()
    
if __name__ == '__main__':
    unittest.main(warnings='ignore')
        