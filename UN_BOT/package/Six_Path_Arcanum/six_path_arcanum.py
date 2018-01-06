
from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'

class six_path_arcanum:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions
		self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'six_path_arcanum', 'open'))

	def __call__(self):
		return self

	def claim(self):
		sleep(4)
		self.mouse.move(self.positions.parse(_POSITIONS, 'six_path_arcanum', 'claim_all'))
		sleep(2)
		self.mouse.move(self.positions.parse(_POSITIONS, 'six_path_arcanum', 'close'))