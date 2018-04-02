import time 
import os
import pyautogui

from datetime import datetime, timedelta
from PIL import ImageGrab, ImageChops, Image

_POSITIONS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\positions.ini'
_SETTINGS = os.path.join(os.path.dirname(os.getcwd()))  + '\\UNLIMITED_NINJA_BOT\settings\settings.ini'

class check:

	def __init__(self, positions, _time):
		self.positions = positions
		self.time = _time

	def __call__(self):
		return self


	def reset(self):
		# arena reset
		if(self.time.isNowInTimePeriod(datetime.strptime(self.positions.parse(_SETTINGS,'arena','fights_reset_time')[1],'%H:%M:%S%p').strftime('%H:%M:%S%p'), datetime.strptime(self.positions.parse(_SETTINGS,'arena','fight_time')[1],'%H:%M:%S%p').strftime('%H:%M:%S%p'))):
	 		self.positions.write(_SETTINGS,'arena','fights_today', 0)
	 		self.positions.write(_SETTINGS,'arena','claimed', 0)


	def master_reset(self):
		self.positions.write(_SETTINGS,'claim','check_in', 0)
		self.positions.write(_SETTINGS,'claim','kaguya_power', 0)
		self.positions.write(_SETTINGS,'claim','profile', 0)
		self.positions.write(_SETTINGS,'claim','vip', 0)
		self.positions.write(_SETTINGS,'daily_benefit','done', 0)
		self.positions.write(_SETTINGS,'dungeon','done', 0)
		self.positions.write(_SETTINGS,'elite_match','done', 0)
		self.positions.write(_SETTINGS,'forbidden_jutsu','done', 0)
		self.positions.write(_SETTINGS,'guild','injects', 0)
		self.positions.write(_SETTINGS,'guild','donate_done', 0)
		self.positions.write(_SETTINGS,'loto','done', 0)
		self.positions.write(_SETTINGS,'lost_tower','done', 0)
		self.positions.write(_SETTINGS,'mount_myobuku','done', 0)
		self.positions.write(_SETTINGS,'occult_techniques','done', 0)
		self.positions.write(_SETTINGS,'samsara_land','done', 0)
		self.positions.write(_SETTINGS,'six_path_arcanum','done', 0)
		self.positions.write(_SETTINGS,'sage_heirloom','done', 0)
		self.positions.write(_SETTINGS,'top_kages','done', 0)
		self.positions.write(_SETTINGS,'wings','done', 0)

	def disconnect(self):
		return self.screenGrab(self.positions.parse(_POSITIONS, 'check', 'disconnect_x_1'),self.positions.parse(_POSITIONS, 'check', 'disconnect_y_1'),"disconnect")

	def gedo_seal(self):
		return self.screenGrab(self.positions.parse(_POSITIONS, 'check', 'gedo_seal_x'),self.positions.parse(_POSITIONS, 'check', 'gedo_seal_y'),"gedo_seal")

	def gedo_10_tails(self):
		return self.screenGrab(self.positions.parse(_POSITIONS, 'check', 'gedo_10_tails_x'),self.positions.parse(_POSITIONS, 'check', 'gedo_10_tails_y'),"gedo_10_tails")

	def dungeon_end(self):
		return self.screenGrab(self.positions.parse(_POSITIONS, 'dungeon', 'time_x'),self.positions.parse(_POSITIONS, 'dungeon', 'time_x'),"dung_time")

	def screenGrab(self,pos1, pos2, method):
		box = []
		box.append(float(pos1[0]))
		box.append(float(pos1[1]))
		box.append(float(pos2[0]))
		box.append(float(pos2[1]))
		
		
		if method == "disconnect":
			dcbutton = pyautogui.locateOnScreen(os.getcwd() + '\\img\\disconnect_1.png')
			if dcbutton != None:
				return True
		elif method == "gedo_seal":
			gedo = pyautogui.locateOnScreen(os.getcwd() + '\\img\\gedo_seal.png')
			if gedo != None:
				return True

		elif method == "gedo_10_tails":
			gedo = pyautogui.locateOnScreen(os.getcwd() + '\\img\\gedo_10_tails.png')
			if gedo != None:
				return True

		elif method == "dung_time":
			gedo = pyautogui.locateOnScreen(os.getcwd() + '\\img\\dung_time_end.png')
			if gedo != None:
				return True

		return False

		
