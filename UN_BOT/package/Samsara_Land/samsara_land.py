from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\v6\settings\positions.ini'

class samsara_land():
	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions
		self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'samsara_land', 'open'))

	def method(self, method):
		if method == "normal":
			self.normal()
		elif method == "scary":
			self.scary()
		elif method == "nightmare":
			self.nightmare()
		elif method == "ri_normal":
			self.ri_normal()
		elif method == "ri_scary":
			self.ri_scary()
		elif method == "ri_nightmare":
			self.ri_nightmare()

	def normal(self):
		pass
		
	def scary(self):
		pass

	def nightmare(self):
		sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'samsara_land', 'nightmare_auto_challenge'))
		sleep(32)
		self.mouse.move(self.positions.parse(_POSITIONS, 'samsara_land', 'confirm')) 

	def ri_normal(self):
		pass

	def ri_scary(self):
		pass

	def ri_nightmare(self):
		pass 	

	def wheel_of_fate(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'samsara_land', 'wheel_of_fate'))
		sleep(2)
		self.mouse.move(self.positions.parse(_POSITIONS, 'samsara_land', 'wheel_of_fate_spin'))
		sleep(2)
		self.mouse.move(self.positions.parse(_POSITIONS, 'samsara_land', 'wheel_of_fate_close'))
		sleep(1)

	def rinne_six_path(self):
		pass

	def close(self):
		sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'samsara_land', 'close'))
		
		