
from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class sage_heirloom:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions

		

	def __call__(self):
		return self


	def claim(self):
		if eval(str(self.positions.parse(_SETTINGS, 'sage_heirloom', 'done')[0])) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'sage_heirloom', 'open'))
			sleep(4)
			self.mouse.move(self.positions.parse(_POSITIONS, 'sage_heirloom', 'r1'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'sage_heirloom', 'r2'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'sage_heirloom', 'claim'))
			sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'sage_heirloom', 'close'))
			sleep(3)
			self.positions.write(_SETTINGS,'sage_heirloom','done', 1)
		else:
			print "[+] Sage Heirloom : Complete"