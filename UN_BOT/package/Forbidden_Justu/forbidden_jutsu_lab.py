
from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'

class forbidden_jutsu_lab:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions

		self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
		print "[+] Forbidden Jutsu Lab : Open"
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'forbidden_jutsu_lab', 'open'))

	def __call__(self):
		return self

	def claim(self):
		print "[+] Forbidden Jutsu Lab : Claim"
		sleep(4)
		self.mouse.move(self.positions.parse(_POSITIONS, 'forbidden_jutsu_lab', 'claim'))
		print "[+] Forbidden Jutsu Lab : Close"
		sleep(2)
		self.mouse.move(self.positions.parse(_POSITIONS, 'forbidden_jutsu_lab', 'close'))