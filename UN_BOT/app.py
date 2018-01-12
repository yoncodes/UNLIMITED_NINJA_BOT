from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from package.Claim import claim
from package.Forbidden_Justu import forbidden_jutsu_lab as FJL
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

# Import Hack
import os, sys, inspect

import time

from function.connection import connection
from function.mouse import mouse
from function.keyboard import keyboard
from function.positions import positions
from function.window import Window as window
from function.notify import popup
from function.countdown import countdown
from function._time import _time
from function.check import check

import updater as update

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

_POSITIONS = parentdir + '\settings\positions.ini'
_SETTINGS = parentdir + '\settings\settings.ini'

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

	def windows_ballon(self, title, msg):
		self.popup.ShowWindow(title, msg)

	def show_window(self):
		self.window.set_up(".*Unlimited Ninja - .*")

	def move(self, cord):
		self.mouse.mousePos(cord)
		self.mouse.leftClick()

	def cord(self):
		self.mouse.get_cords()

	def commands(self, cmd):
		self.keyboard.type(cmd)

	def system_checks(self):
		self.check = check(self.positions, self.time)
		return self.check()

	def update(self):
		self.update = update.updater()

		if eval(str(self.positions.parse(_SETTINGS, 'update', 'auto')[0])):
			self.update.check()
		else:
			print "[+] Auto Update disabled"

	def start(self):
		pass

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
		if eval(str(self.positions.parse(_SETTINGS, 'daily_benefit', 'done')[0])) != True:
			self.daily_benefit = daily_benefit.daily_benefit(self.mouse, self.positions)
			self.positions.write(_SETTINGS,'daily_benefit','done', 1)
			return self.daily_benefit()
		else:
			print "[+] Daily benefit : Complete"

	def dungeon(self):
		if eval(str(self.positions.parse(_SETTINGS, 'dungeon', 'done')[0])) != True:
			self.Dungeon = dungeon.dungeon(self.mouse, self.positions)
			self.positions.write(_SETTINGS,'dungeon','done', 1)
			return self.Dungeon()
		else:
			print "[+] Dungeon : Complete"

	def eight_gates(self):
		pass

	def elite_match(self):
		if eval(str(self.positions.parse(_SETTINGS, 'elite_match', 'done')[0])) != True:
			self.elite_match = elite_match.elite_match(self.mouse,self.positions)
			self.positions.write(_SETTINGS,'elite_match','done', 1)
			return self.elite_match()

	def forbidden_jutsu(self):
		if eval(str(self.positions.parse(_SETTINGS, 'forbidden_jutsu', 'done')[0])) != True:
			self.forbidden_jutsu_lab = FJL.forbidden_jutsu_lab(self.mouse, self.positions)
			self.positions.write(_SETTINGS,'forbidden_jutsu','done', 1)
			return self.forbidden_jutsu_lab()
		else:
			print "[+] Forbdden Justu Lab : Complete"
		pass


	def guild(self):
		pass

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
		pass

	def loto(self):
		# Legends of the Oracles
		if eval(str(self.positions.parse(_SETTINGS, 'loto', 'done')[0])) != True:
			self.land_of_oracles = land_of_oracles.land_of_oracles(self.mouse, self.positions)
			self.positions.write(_SETTINGS,'loto','done', 1)
			return self.land_of_oracles()
		else:
			print "[+] Land Of Oracles : Complete"

	def lost_tower(self):
		self.countdown.timer(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'functions', 'hover'))
		self.countdown.timer(5)
		self.mouse.move(self.positions.parse(_POSITIONS, 'lost_tower', 'open'))
		self.countdown.timer(2)
		self.mouse.move(self.positions.parse(_POSITIONS, 'lost_tower', 'lvl_105'))
		self.countdown.timer(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'lost_tower', 'lvl_105_auto'))
		self.countdown.timer(32)
		self.mouse.move(self.positions.parse(_POSITIONS, 'lost_tower', 'confirm'))
		self.countdown.timer(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'lost_tower', 'lvl_close'))
		self.countdown.timer(1)
		self.mouse.move(self.positions.parse(_POSITIONS, 'lost_tower', 'close'))
		self.countdown.timer(1)


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
		pass

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
		if eval(str(self.positions.parse(_SETTINGS, 'six_path_arcanum', 'done')[0])) != True:
			self.six_path_arcanum = six_path_arcanum.six_path_arcanum(self.mouse, self.positions)
			self.positions.write(_SETTINGS,'six_path_arcanum','done', 1)
			return self.six_path_arcanum()
		else:
			print "[+] Six Path Arcanum : Complete"

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
		if eval(str(self.positions.parse(_SETTINGS, 'top_kages', 'done')[0])) != True:
			self.wings = wings.wings(self.mouse, self.positions)
			self.positions.write(_SETTINGS,'wings','done', 1)
			return self.wings().claim()
		else:
			print "[+] Wings : Complete"