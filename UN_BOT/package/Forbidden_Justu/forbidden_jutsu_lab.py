
from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class forbidden_jutsu_lab:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions

		

	def __call__(self):
		return self

	def claim(self):
		if eval(str(self.positions.parse(_SETTINGS, 'forbidden_jutsu', 'done')[0])) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'forbidden_jutsu_lab', 'open'))
			sleep(4)
			self.mouse.move(self.positions.parse(_POSITIONS, 'forbidden_jutsu_lab', 'claim'))
			sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'forbidden_jutsu_lab', 'close'))
			self.positions.write(_SETTINGS,'forbidden_jutsu','done', 1)
		else:
			print "[+] Forbidden Justu Lab : Complete"
			#self.mouse.move(self.positions.parse(_POSITIONS, 'forbidden_jutsu_lab', 'close'))