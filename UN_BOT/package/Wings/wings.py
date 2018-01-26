import time

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'

class wings:
	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions
		
		self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
		time.sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'wings', 'open'))
		time.sleep(2)

	def __call__(self):
		return self

	def claim(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'wings', 'enhance'))
		
		wing = 0
		while wing < 20:
			self.mouse.move(self.positions.parse(_POSITIONS,'wings','silver_claim'))
			time.sleep(.5)
			wing += 1

		time.sleep(2)

		self.mouse.move(self.positions.parse(_POSITIONS, 'wings', 'firewing_cave'))

		time.sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'wings', 'normal'))
		time.sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'wings', 'nightmare'))
		time.sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'wings', 'claim'))
		time.sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'wings', 'hard'))
		time.sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'wings', 'claim'))
		time.sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'wings', 'close'))