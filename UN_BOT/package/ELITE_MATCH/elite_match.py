from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'

class elite_match:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions

		self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
		print "[+] Elite Match : Open"
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'open'))

	def __call__(self):
		return self

	def toast(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'toast'))
		sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'toast_plum'))
		sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'toast_close'))
		sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'join'))
		sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'elite_match', 'close'))
		sleep(1)