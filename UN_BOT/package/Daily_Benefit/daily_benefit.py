from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\v6\settings\positions.ini'

class daily_benefit:
	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions

		self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'open'))

	def __call__(self):
		return self

	def claim(self, extra=False):
		self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'open'))
		sleep(1)
		if extra == False:
			self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'free_retrieve_all'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'daily_benefit'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'reward_1'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'reward_2'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'reward_3'))
			sleep(1)
		else:
			self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'gold_retrieve_all'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'daily_benefit'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'reward_1'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'reward_2_extra'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'reward_2'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'reward_3_extra'))
			sleep(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'reward_3'))
			sleep(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'daily_benefits', 'close'))