import re
import itertools as it
import sys
import math
import os
import glob

class list_writer():
	global list_of_lists
	global generated_list
	
	with open('data.txt', 'r') as text_file:
		lines = text_file.readlines()
	
	list_of_lists = []
	stats_text = lines[0]
	generated_list = []
	
	def __init__(self):
		list_writer.POINT_MAXIMUM = 0
		list_writer.points = 0
		list_writer.added_value = 0

	def main(self):
		self.main_menu()

	def main_menu(self):
		print("WELCOME TO 40K LIST BUILDER\nSELECT BELOW OPTION")
		print("1. NEW LIST\n2. LOAD LIST\n3. DELETE LIST\n4. EXIT")
		user = input("")
		if user.isdigit():
			if user == "1":
				commonFunctions.parse_profiles()
				self.main_option_1()
			elif user == "2":
				self.main_option_2()
			elif user == "3":
				self.main_option_3()
			elif user == "4":
				commonFunctions.exit_program()
			else:
				self.main_menu()
		else:
			self.main_menu()
					
	def main_option_1(self):
		self.point_max()
		while(True):
			print("Make unit selection\nEnter 'r' to remove selection\nEnter 'e' to exit the program")
			commonFunctions.display_units(list_of_lists)
			user = input("")
			if user == "e":
				commonFunctions.exit_program()
			elif user == "s":
				commonFunctions.save_list()
			elif user == "m":
				self.main_menu()
			self.parse_input(user)
			commonFunctions.format_units(generated_list)	
			self.points_cost(list_of_lists, user)
			print("%s / %s" % (self.points, self.POINT_MAXIMUM))
			print("")

	def main_option_2(self):
		FILES = []
		commonFunctions.display_files()
		FILES = glob.glob('./*.wl')
		print("Select file to load")
		print("Enter file number")
		user = input("")
		OPEN_FILE = open(FILES[int(user)-1], "r+")
		with OPEN_FILE as text_file:
			print(text_file.readlines())
		
	def main_option_3(self):
		commonFunctions.display_files()
		print("Enter file number to delete\nEnter 'm' to return to menu\nEnter 'e' to exit the program")
		user = input("")
		while(True):
			if user.isdigit():
				if int(user) > len(TEXT_FILES) or int(user) == 0:
					print("ERROR : PLEASE MAKE A SELECTION FROM THE LIST")
					break
				elif int(user) <= len(TEXT_FILES):
					os.remove(TEXT_FILES[int(user) - 1])
					return
			elif user == "e":
				commonFunctions.exit_program()
				self.main_option_3()
			elif user == "m":
				self.main_menu()
			else:
				print("ERROR : PLEASE MAKE A SELECTION FROM THE LIST")
				self.main_option_3()
		
	def parse_input(self, user):
		if user.isdigit():	
			if int(user) > len(list_of_lists) or int(user) <= 0 :
				print("ERROR: ENTER POSITIVE VALUE FROM 1 - %s" % (len(list_of_lists)))
			else:
				generated_list.append(list_of_lists[int(user) - 1])
		elif user == "r":
			commonFunctions.remove_from_list(generated_list)
		else:
			print("Enter a number corresponding to a unit")
			
	def point_max(self):
		while(True):
			print("Please enter a positive integer value for your point maximum. For no limit, enter '0'")
			user = input("")
			if user.isdigit():
				if int(user) > 0:
					self.POINT_MAXIMUM = user
					print(self.POINT_MAXIMUM)
					break
				elif int(user) == 0:
					self.POINT_MAXIMUM = math.inf
					print(self.POINT_MAXIMUM)
					break
				else:
					print("ERROR : PLEASE ENTER A VALUE FOR YOUR POINTS MAXIMUM")
					break
			else:
				print("ERROR : PLEASE ENTER A VALUE FOR YOUR POINTS MAXIMUM")
	
	def points_cost(self, list_creation, user):
		if user.isdigit():
			if int(user) <= len(list_creation) and int(user) > 0:
				self.points += int(list_creation[int(user) - 1][0])

class commonFunctions(list_writer):
	def remove_from_list(user_list):
		print("Which selection will you remove?")
		units = []
		for i in range(len(user_list)):
			units.append(user_list[i][2].strip())
			num = units[i]
			print("%s. %s" % (i+1, num))
		user = input("")
		if user.isdigit():
			if int(user) > len(user_list) or int(user) == 0:
				print("ERROR : PLEASE MAKE SELECTION FROM LIST")
			elif int(user) <= len(user_list):
				list_writer.points -= int(generated_list[int(user)-1][0])
				del user_list[int(user) - 1]
		else:
			print("ERROR : PLEASE MAKE SELECTION FROM LIST")
	
	@staticmethod			
	def exit_program():
		while(True):
			print("CONFIRM EXIT PROGRAM: Y/N")
			user = input("")
			if user == 'y' or user == 'Y':
				print("Exiting program")
				sys.exit()
			elif user == 'n' or user == 'N':
				break
			else:
				print("ERROR : INVALID SELECTION")	
	
	def display_units(options):
		units = []
		for i in range(len(options)):
			units.append(options[i][2].strip())
			num = units[i]  
			print("%s. %s" % (i+1, num))
			
	def format_stats(stat=None):
		TEMPLATE = '|%s|'
		print(TEMPLATE % stat, end='')
		
	def parse_profiles():
		for key,group in it.groupby(list_writer.lines, lambda line: line.startswith('+')):
			if not key:
				group = list(group)
				list_of_lists.append(group)

	def format_units(list):
		for i in range(len(list)):
			print(list[i][2].strip())
	
	def save_list():
		print("INPUT FILE NAME")
		user = input("")
		FILENAME = user + ".wl"
		file = open(FILENAME, "w+")
		text = "".join(str(elm) for elm in generated_list)
		file.write(text)
	
	def display_files():
		FILES = glob.glob('./*.wl')
		for i in range(len(FILES)):
			FILES[i].strip('..\\')
			print("%s. %s" % (i+1, FILES[i]))

if __name__ == '__main__':
	list_writer().main()
		
	
		