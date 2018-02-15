from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'

class top_kages:
	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions

		self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'top_kages', 'open'))
		sleep(2)

	def practice(self, practice, ri):
		kages = ['kazekage', 'mizukage', 'tsuchikage', 'raikage', 'hokage', '4th_hokage', '1st_hokage', 'mystical_shadow', '2nd_tsuchikage', '6th_hokage', '7th_hokage']
		stop = len(kages) if practice == 'all' else kages.index(practice)+1

		for e in range(0,stop):
			self.mouse.move(self.positions.parse(_POSITIONS, 'top_kages', kages[e]))
			sleep(1)

			if (e >6 and not ri):
				pass
		self.mouse.move(self.positions.parse(_POSITIONS, 'top_kages', 'close'))
		sleep(1)
