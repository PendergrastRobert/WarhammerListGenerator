import re

class list_writer():
	text_file = open("data.txt", "r")
	lines = text_file.readlines()
	
	def set_stats(self):
		stats_text = self.lines[0]
		stats_list = list(filter(None, re.split(';|, |\n', stats_text)))
		
		self.movement = stats_list[0]
		self.weapon_skill = stats_list[1]
		self.ballistic_skill = stats_list[2]
		self.strength = stats_list[3]
		self.wounds = stats_list[4]
		self.attacks = stats_list[5]
		self.leadership = stats_list[6]
		self.save = stats_list[7]
		self.invul_save = stats_list[8]
		
		print(stats_list)
		print(self.invul_save)
	def set_name(self):
		name = self.lines[1].strip()
		print(name)
		
	def set_equipment(self):
		equipment = self.lines[2].strip()
		print(equipment)
		
	def set_armour(self):
		armour = self.lines[3].strip()
		print(armour)
		
	def print_values(self):
		self.set_stats()
		self.set_name()
		self.set_equipment()
		self.set_armour()
		
lw = list_writer()
lw.print_values()	
	
	
		