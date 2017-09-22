#!/usr/bin/env python

from util import *




class AllTestCases(unittest.TestCase):
	
	def setUp(self):
		self.testbase = TestBase()
		self.testbase.goto("http://selenium-python.readthedocs.io/api.html")
	

	def test_Page_Title(self):
		browser_title = self.testbase.get_title()
		self.assertIn("Selenium Python Bindings 2 documentation" , browser_title)

	@unittest.skip("demonstrating skipping")
	def test_nothing(self):
		self.fail("shouldn't happen")

	def tearDown(self):
		self.testbase.close_browser()

	



if __name__ == '__main__':
	unittest.main(verbosity=2)