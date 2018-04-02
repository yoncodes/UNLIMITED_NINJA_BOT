from package.Claim import claim
from package.Forbidden_Justu import forbidden_jutsu_lab
from package.Six_Path_Arcanum import six_path_arcanum
from package.Samsara_Land import samsara_land
from package.Top_Kages import top_kages
from package.Treasure_Map import treasure_map
from package.Arena import arena
from package.Dungeon import dungeon
from package.Daily_Benefit import daily_benefit
from package.Land_Of_Oracles import land_of_oracles
from package.Wings import wings
from package.Mail import mail
from package.ELITE_MATCH import elite_match
from package.Konoha import konoha
from package.Sage_Heirloom import sage_heirloom
from package.Guild import guild
from package.Lost_Tower import lost_tower
from package.Yggdrassil import yggdrassil

from selenium import webdriver
from sys import platform as _platform

# Import Hack
import os, sys, inspect

import time

from function.connection import connection

# temp fix for mac users
if _platform == "win32" or _platform =="win64":
	from function.mouse import mouse
elif _platform == "darwin":
	from function.mouseMac import mouseMac as mouse

from function.keyboard import keyboard
from function.positions import positions
from function.window import Window as window
from function.notify import popup
from function.countdown import countdown
from function._time import _time
from function.check import check
from function.schedule import schedule
from function.auth import Auth


import updater as update

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

if _platform == "win32" or _platform =="win64":
	_POSITIONS = parentdir + '\settings\positions.ini'
	_SETTINGS = parentdir + '\settings\settings.ini'
	_BROWSER = parentdir + '\\browser\chromedriver.exe'
elif _platform == "darwin":
	_POSITIONS = parentdir + '/settings/positions.ini'
	_SETTINGS = parentdir + '/settings/settings.ini'
	_BROWSER = parentdir + '/browser/chromedriver'

class app:

	def __init__(self):
		self.connection = connection()
		self.mouse = mouse()
		self.keyboard = keyboard()
		self.positions = positions()
		self.window = window()
		self.popup = popup()
		self.countdown = countdown()
		self.time = _time()
		self.schedule = schedule()
		

		

	def windows_ballon(self, title, msg):
		self.popup.ShowWindow(title, msg)

	def show_window(self,platform):
		self.window.set_up(platform)

	def move(self, cord):
		self.mouse.mousePos(cord)
		self.mouse.leftClick()

	def cord(self):
		self.mouse.get_cords()

	def drag_n_drop(self,current_pos, new_pos):
		self.mouse.drag_n_drop(current_pos, new_pos)

	def commands(self, cmd):
		self.keyboard.type(cmd)

	def position(self):
		return self.positions

	def system_checks(self):
		self.check = check(self.positions, self.time)
		return self.check()

	def update(self):
		self.update = update.updater()

		if eval(str(self.positions.parse(_SETTINGS, 'update', 'auto')[0])):
			self.update.check()
		else:
			print "[+] Auto Update disabled"


	def start(self, username, password, server, platform):
		# set up chrome browser
		prefs = {
		    "profile.default_content_setting_values.plugins": 1,
		    "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
		    "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
		    "PluginsAllowedForUrls": "http://ninja.joyfun.com"
		}

		self.chrome_options = webdriver.ChromeOptions()
		self.chrome_options.add_argument('--disable-infobars')
		self.chrome_options.add_experimental_option("prefs",prefs)
		self.driver = webdriver.Chrome(executable_path=_BROWSER,chrome_options=self.chrome_options)

		self.auth = Auth(self.driver, self.mouse, self.positions, self.window)
		self.auth.login(username, password, server, platform)

	def arena(self):
		"""
		arena.fights(5)
		arena.claim(true)

		"""
		self.arena1 = arena.arena(self.mouse, self.positions, self.time)
		return self.arena1()
		

	def claim(self):
		self.claim1 = claim.claim(self.mouse, self.positions)
		return self.claim1

	def daily_benefit(self):
	
		self.daily_benefit = daily_benefit.daily_benefit(self.mouse, self.positions)
		return self.daily_benefit()

	def dungeon(self):
		
		self.Dungeon = dungeon.dungeon(self.mouse, self.positions, self.system_checks)
		return self.Dungeon()
		
	def eight_gates(self):
		pass

	def elite_match(self):
		
		self.elite_match = elite_match.elite_match(self.mouse,self.positions, self.time)
			
		return self.elite_match()

	def forbidden_jutsu(self):
		
		self.forbidden_jutsu_lab1 = forbidden_jutsu_lab.forbidden_jutsu_lab(self.mouse, self.positions)
		return self.forbidden_jutsu_lab1()
		
	def guild(self):
		self.guild = guild.guild(self.mouse, self.keyboard, self.positions, self.time)
		return self.guild()

	def jinchuriki_awakening(self):
		pass

	def konoha(self):
		"""

		konoha.conquest.form()
		konoha.conquest.go()
		konoha.conquest.end()

		konoha.defense.go()
		konoha.defense.check()
		konoha.defense.end()

		"""
		self.konoha1 = konoha.konoha(self.mouse, self.positions) 

	def loto(self):
		# Legends of the Oracles
		
		self.land_of_oracles = land_of_oracles.land_of_oracles(self.mouse, self.positions)
			
		return self.land_of_oracles()
	

	def lost_tower(self):
		self.lost_tower1 = lost_tower.lost_tower(self.mouse, self.positions)
		return self.lost_tower1()


	def mail(self):
		self.mail = mail.mail(self.mouse, self.positions)
		return self.mail()

	def mall(self):
		pass

	def master_n_slave(self):
		pass

	def mount_myobuku(self):
		if eval(str(self.positions.parse(_SETTINGS, 'mount_myobuku', 'done')[0])) != True:
			self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
			self.countdown.timer(3)
			self.mouse.move(self.positions.parse(_POSITIONS, 'mount_myobuku', 'open'))
			self.countdown.timer(5)
			self.mouse.move(self.positions.parse(_POSITIONS, 'mount_myobuku', 'practice'))
			self.countdown.timer(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'mount_myobuku', 'support_wings'))
			self.countdown.timer(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'mount_myobuku', 'fairy_training'))
			self.countdown.timer(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'mount_myobuku', 'fairy_training_confirm'))
			self.countdown.timer(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'mount_myobuku', 'down'))
			self.countdown.timer(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'mount_myobuku', 'army'))
			self.countdown.timer(1)

			training = 0
			while training < 5:
				self.mouse.move(self.positions.parse(_POSITIONS, 'mount_myobuku', 'silver_training'))
				self.countdown.timer(1)
				training += 1

			self.mouse.move(self.positions.parse(_POSITIONS, 'mount_myobuku', 'close'))
			self.positions.write(_SETTINGS,'mount_myobuku','done', 1)
		else:
			print "[+] Mount Myobuku : Complete"

	def ninja_clash(self):
		pass

	def ninja_wings(self):
		pass

	def occult_techniques(self, harvest=3):
		if eval(str(self.positions.parse(_SETTINGS, 'occult_techniques', 'done')[0])) != True:
			self.countdown.timer(1)
			self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
			self.countdown.timer(5)
			self.mouse.move(self.positions.parse(_POSITIONS, 'occult_techniques', 'open'))
			self.countdown.timer(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'occult_techniques', 'aquire'))
			self.countdown.timer(2)

			times = 0
			while times < harvest:
				self.mouse.move(self.positions.parse(_POSITIONS, 'occult_techniques', 'harvest'))
				self.countdown.timer(2)
				self.mouse.move(self.positions.parse(_POSITIONS, 'occult_techniques', 'reset'))
				self.countdown.timer(2)
				times += 1
			self.mouse.move(self.positions.parse(_POSITIONS, 'occult_techniques', 'reset'))
			self.countdown.timer(2)
			self.mouse.move(self.positions.parse(_POSITIONS, 'occult_techniques', 'close'))
			self.positions.write(_SETTINGS,'occult_techniques','done', 1)
		else:
			print "[+] Occult Techniques : Complete"

	def realms(self):
		pass

	def rebels(self):
		pass

	def sage_heirloom(self):
		self.sage_heirloom1 = sage_heirloom.sage_heirloom(self.mouse, self.positions)
		return self.sage_heirloom1()


	def samsara_land(self, land="nightmare"):
		if eval(str(self.positions.parse(_SETTINGS, 'samsara_land', 'done')[0])) != True:
			self.samsara_land = samsara_land.samsara_land(self.mouse,self.positions)
			self.countdown.timer(5)
			self.samsara_land.method(land)
			self.countdown.timer(2)
			self.samsara_land.wheel_of_fate()
			self.countdown.timer(2)
			self.samsara_land.close()
			self.positions.write(_SETTINGS,'samsara_land','done', 1)
		else:
			print "[+] Samsara Land : Complete"

	def six_path_arcanum(self):
		
		self.six_path_arcanum = six_path_arcanum.six_path_arcanum(self.mouse, self.positions)
		return self.six_path_arcanum()

	def special_events(self, data):
		pass

	def taboo_justu(self):
		pass

	def treasure_map(self):
		self.treasure_map1 = treasure_map.treasure_map(self.mouse,self.positions,self.keyboard,self.time)
		return self.treasure_map1()

	def top_kages(self, ri=True, practice='all'):
		if eval(str(self.positions.parse(_SETTINGS, 'top_kages', 'done')[0])) != True:

			self.top_kages = top_kages.top_kages(self.mouse,self.positions)
			self.top_kages.practice(practice, ri)
			self.positions.write(_SETTINGS,'top_kages','done', 1)
		else:
			print "[+] Top Kages : Complete"

	def tournament(self):
		pass

	def ultimate_challenge(self):
		pass 

	def wings(self):
		
		self.wings = wings.wings(self.mouse, self.positions)
			
		return self.wings().claim()

	def yggdrassil(self):

		self.yggdrassil = yggdrassil.yggdrassil(self.mouse, self.positions)

		return self.yggdrassil()
		