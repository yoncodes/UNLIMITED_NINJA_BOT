# -*- coding: utf-8 -*-
from selenium import webdriver

import os.path

BROWSER = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\\browser\\chromedriver.exe'

class browser:

	def __init__(self):
		self.UN_BROWSE()

	def UN_BROWSE(self):
		self.chrome_options = webdriver.ChromeOptions()
		self.chrome_options.add_argument('--disable-infobars')
		self.driver = webdriver.Chrome(executable_path=BROWSER,chrome_options=self.chrome_options)
		return self.driver