import time 
import os.path

from datetime import datetime, timedelta

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class treasure_map:

	def __init__(self, mouse, positions, keyboard, time1):
		self.mouse = mouse
		self.keyboard = keyboard
		self.positions = positions
		self.time = time1

	def __call__(self):
		return self

	def hunt(self):
		print "[+] Treasure Map"

		current = self.positions.parse(_SETTINGS, 'treasure_map', 'hunt')[0]
		is_complete = self.positions.parse(_SETTINGS, 'treasure_map', 'is_complete')[0]
		last_time = self.positions.parse(_SETTINGS, 'treasure_map', 'last_time')[0]
		twenty_one_min = datetime.now() + timedelta(minutes=21)
		forty_min = twenty_one_min + timedelta(minutes=20)
		twenty_one_min = '{:%H:%M:%S%p}'.format(twenty_one_min)
		
		#print datetime.strptime(self.positions.parse(_SETTINGS,'treasure_map','last_time')[1],'%H:%M:%S%p').strftime('%H:%M:%S%p')
		
		if bool(eval(is_complete)) != True:
			if eval(current) < 5:
				if self.time.isNowInTimePeriod(datetime.strptime(self.positions.parse(_SETTINGS,'treasure_map','last_time')[1],'%H:%M:%S%p').strftime('%H:%M:%S%p'), forty_min.strftime('%H:%M:%S%p')):
					self.mouse.move(self.positions.parse(_POSITIONS,'treasure_map','open'))
					time.sleep(3)
					self.mouse.move(self.positions.parse(_POSITIONS,'treasure_map','hunt'))
					time.sleep(2)

					silver = 0
					
					while silver < 5:
						self.mouse.move(self.positions.parse(_POSITIONS,'treasure_map','silver'))
						time.sleep(.5)
						silver += 1
					
					time.sleep(2)
					self.mouse.move(self.positions.parse(_POSITIONS,'ninja_rank','close')) # Annoying pop up close

					time.sleep(.5)

					self.mouse.move(self.positions.parse(_POSITIONS,'treasure_map','start'))
					time.sleep(2)

					self.keyboard.space()
					time.sleep(2.4) # Find out correct timing
					self.keyboard.space()

					time.sleep(2)
					self.mouse.move(self.positions.parse(_POSITIONS,'treasure_map','map_close'))

					time.sleep(.1)

					self.mouse.move(self.positions.parse(_POSITIONS,'treasure_map','close'))
					
					current = int(current)
					current += 1
					self.positions.write(_SETTINGS,'treasure_map','hunt', int(current))
					self.positions.write(_SETTINGS,'treasure_map','last_time', twenty_one_min)

				elif(int(self.positions.parse(_SETTINGS,'treasure_map','hunt')[0]) == 5):
						self.positions.write(_SETTINGS,'treasure_map','is_complete', 1)
				else:
					print "[+] Time Remaining {}".format(self.time.until(datetime.now().time().strftime('%H:%M:%S%p'), datetime.strptime(self.positions.parse(_SETTINGS,'treasure_map','last_time')[1],'%H:%M:%S%p').strftime('%H:%M:%S%p')))
		if (int(self.positions.parse(_SETTINGS,'treasure_map','hunt')[0]) != 5):
			print "[+] Remaining : " + str(int(self.positions.parse(_SETTINGS,'treasure_map','max_tries')[0])-int(self.positions.parse(_SETTINGS,'treasure_map','hunt')[0]))
		else:
			print "[+] Treasure Map : Complete"