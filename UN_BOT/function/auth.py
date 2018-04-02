import os.path
from time import sleep

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'


class Auth:

	def __init__(self, driver, mouse, positions, window):
		self.driver = driver
		self.mouse = mouse
		self.positions = positions
		self.window = window

	def login(self, username, password, server, platform):
		self.driver.implicitly_wait(5)
		if platform == "joyfun":
			self.driver.get("http://ninja.joyfun.com")
			self.driver.find_element_by_id("left_username").send_keys(username)
			self.driver.find_element_by_id("left_password").send_keys(password)
			self.driver.find_element_by_class_name("sub_login_btn").click()
			sleep(3)
			self.driver.find_element_by_class_name("gamestart").click()
			sleep(5)
			self.driver.get('http://ninja.joyfun.com/play/server/' + str(server))
			sleep(5)
			self.window.set_up("joyfun")
			sleep(20)
			self.mouse.move(self.positions.parse(_POSITIONS, 'browser', 'pop_up_close'))
			sleep(.5)
			self.mouse.move(self.positions.parse(_POSITIONS, 'browser', 'disable_music'))
			sleep(2)
			self.driver.execute_script("document.querySelector('.close_adbtn').click();")
		elif platform == "plaync100":
			self.driver.get('http://www.plaync100.us//game/ninjaworld/play/' +str(server))
			sleep(6)
			self.driver.find_element_by_id("email").send_keys(username)
			self.driver.find_element_by_id("password").send_keys(password)
			self.driver.find_element_by_xpath("//*[@type='submit']").submit()
			sleep(10)

		elif platform == "fb":
			self.driver.get("https://www.plaync100.us/user/login")
			sleep(6)
			self.driver.find_element_by_id("email").send_keys(username)
			self.driver.find_element_by_id("password").send_keys(password)
			self.driver.find_element_by_xpath("//*[@type='submit']").submit()
			sleep(2)
			self.driver.get('http://www.plaync100.us/game/ninjaworld/play/' +str(server) +'/psrc/JCfacebook')
			sleep(8)
			self.driver.execute_script("document.getElementById('header').remove();")
			


	def __call__(self, value=[]):
		pass