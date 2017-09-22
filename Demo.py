
import os
import unittest
import doctest
from selenium import webdriver

class Testing:

	def __init__(self):
		self.browser = webdriver.Chrome(os.getcwd()+"/chromedriver")

	def goto(self,url):
		self.browser.get(url)

	def get_title(self):
		browser_title = self.browser.title
		return browser_title

	def close_browser(self):
		self.browser.quit()



class TestCases(unittest.TestCase):

	def setUp(self):
		self.test = Testing()
		self.test.goto("http://selenium-python.readthedocs.io/api.html")

	def test_Page_Title(self):
		browser_title = self.test.get_title()
		self.assertIn("Selenium Python Bindings 2 documentation",browser_title)

	def teadDown(self):
		self.test.close_browser()

if __name__ == '__main__':
    unittest.main(verbosity=2)


