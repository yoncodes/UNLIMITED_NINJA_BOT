from time import sleep

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'

class mail:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions

	def __call__(self):
		return self

	def check(self, pages):
		page = 0
		print '[+] Checking Mail'
		self.open()
		while page < pages:
			print "[+] Selecting all "
			sleep(.1)
			self.select_all()
			print "[+] Recieving Mail"
			sleep(.1)
			self.recieve()
			sleep(.5)
			print "[+] Deleting Mail"
			sleep(.5)
			self.delete()
			page += 1
		print "[+] Closing Mail"
		self.close()
		sleep(.1)

	def open(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'mail', 'open'))

	def select_all(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'mail', 'select_all'))

	def recieve(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'mail', 'recieve'))

	def delete(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'mail', 'delete'))

	def close(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'mail', 'close'))