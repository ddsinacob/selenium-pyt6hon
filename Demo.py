import os
from selenium import webdriver


browser = webdriver.Chrome(os.getcwd()+"/chromedriver")
browser.get('http://seleniumhq.org/')
