from time import sleep

import datetime

import os.path

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class claim:

	def __init__(self, mouse, positions):
		self.mouse = mouse
		self.positions = positions


	def __call__(self):
		return self

	def online(self):
		self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'time_online_default'))
		sleep(3)
		self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'time_online'))
		sleep(2)
		self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'time_online_close'))
		sleep(.5)

	def check_in(self):
		if eval(str(self.positions.parse(_SETTINGS, 'claim', 'check_in')[0])) != True:
			print "[+] Online : Checking in"
			self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'check_in_default'))
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'check_in'))
			sleep(3)
			print "[+] Online : Claiming Rewards"
			self.mouse.move(self.positions.parse(_POSITIONS,'claim', 'check_in_rewards'))
			sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'check_in_cumulative'))
			sleep(2)
			self.day()
			sleep(1)
			print "[+] Online : Checking in Closing"
			self.mouse.move(self.positions.parse(_POSITIONS, 'claim', 'check_in_close'))
			sleep(.1)
			self.positions.write(_SETTINGS,'claim','check_in', 1)
		else:
			print "[+] Check In : Complete"

	def day(self):
		today = datetime.date.today()
		go = False
		if today.day != 29:
			if today.day != 30:
				if today.day != 31:
					go = True
		if go == True:
			num = self.positions.parse(_POSITIONS, 'online', 'day' + str(today.day))
			print "[+] Online : Claim Day {}".format(today.day)
			self.mouse.move(num)

	def kaguya_power(self):
		if eval(str(self.positions.parse(_SETTINGS, 'claim', 'kaguya_power')[0])) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'kaguya_power', 'open'))
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'kaguya_power', 'claim'))
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'kaguya_power', 'close'))
			sleep(.1)
			self.positions.write(_SETTINGS,'claim','kaguya_power', 1)
		else:
			print "[+] Kaguya Power Claim : Complete"

	def vip(self):
		if eval(str(self.positions.parse(_SETTINGS, 'claim', 'vip')[0])) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'vip', 'open'))
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'vip', 'claim'))
			sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'vip', 'close'))
			sleep(.1)
			self.positions.write(_SETTINGS,'claim','vip', 1)
		else:
			print "[+] Vip Claim : Complete"

	def profile(self):
		if eval(str(self.positions.parse(_SETTINGS, 'claim', 'profile')[0])) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'profile', 'open'))
			sleep(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'profile', 'claim'))
			sleep(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'profile', 'close'))
			sleep(.1)
			self.positions.write(_SETTINGS,'claim','profile', 1)
		else:
			print "[+] Profile Claim : Complete"