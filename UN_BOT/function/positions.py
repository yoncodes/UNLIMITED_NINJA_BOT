import re, os

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.

class positions:

	def __init__(self):
		pass


	def read(self,filename,section, pos):
		config = ConfigParser()
		with open(os.path.join(os.path.dirname(os.getcwd()),filename),'r') as configfile:
			config.readfp(configfile)
	        content = config.get(section, pos)
	        return content

	def write(self,filename,section, pos, data):
		config = ConfigParser()
		config.read(filename)
		config.set(section, pos, data)

		with open(filename, 'w') as configfile:
			config.write(configfile)



	def parse(self, filename, section, pos):
		info = self.read(filename, section, pos)

		method_1 = re.match(r"(\d\d\d\d|\d\d\d|\d\d)x(\d\d\d\d|\d\d\d|\d\d)", info)
		method_2 = re.match(r"([0-9]|[0-9][0-9]|\d\d\d\d)",info)
		method_3 = re.match(r"[0-9][0-9]:[0-9][0-9]:[0-9][0-9](AM|am|PM|pm)", info)

		d = []

		if method_1 is not None: 

			d.append(method_1.group(1))
			d.append(method_1.group(2))
		if method_2 is not None:

			d.append(method_2.group(1))
			

		if method_3 is not None:

			d.append(method_3.group(0))

		return d

	def set_window(self, hwnd, x_axis, y_axis, size_x, size_y):
		pass

	