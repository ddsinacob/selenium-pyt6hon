import os
import unittest
from selenium import webdriver


class TestBase(object):

	def __init__(self):
		self.browser = webdriver.Chrome(os.getcwd()+"/chromedriver")

	def goto(self,url):
		self.browser.get(url)

	def get_title(self):
		browser_title = self.browser.title
		return browser_title

	def close_browser(self):
		self.browser.quit()