from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'

class land_of_oracles:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions

		self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'legend_of_oracles', 'open'))


	def __call__(self):
		return self

	def claim(self, ri=True):
		if ri:
			sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'legend_of_oracles', 'ri1_1'))
			sleep(.5)
			self.mouse.move(self.positions.parse(_POSITIONS, 'legend_of_oracles', 'ri1_2'))
			sleep(.5)
			self.mouse.move(self.positions.parse(_POSITIONS, 'legend_of_oracles', 'ri1_3'))
			sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'legend_of_oracles', 'select'))
			sleep(.5)
			self.mouse.move(self.positions.parse(_POSITIONS, 'legend_of_oracles', 'r2_open'))
			sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'legend_of_oracles', 'ri1_1'))
			sleep(.5)
			self.mouse.move(self.positions.parse(_POSITIONS, 'legend_of_oracles', 'ri1_2'))
			sleep(.5)
			self.mouse.move(self.positions.parse(_POSITIONS, 'legend_of_oracles', 'ri1_3'))
			sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'legend_of_oracles', 'confirm'))
			sleep(.5)
			self.mouse.move(self.positions.parse(_POSITIONS, 'legend_of_oracles', 'close'))

