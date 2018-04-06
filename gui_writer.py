import tkinter as tk
import os
import sys
import subprocess as sub
from writerClass import *

root = tk.Tk()
lw = list_writer()
cf = commonFunctions()

with open('data.txt', 'r') as text_file:
	lines = text_file.readlines()

class Application(tk.Frame):	
	variable = tk.StringVar()
	
	def __init__(self, master):
		super().__init__(master)
		self.create_widgets()

	def create_widgets(self):
		self.tk_main_menu()

	def tk_main_menu(self):
		labelText = tk.StringVar()
		tk.Label(text = "WARHAMMER 40K\n LIST BUILDER").grid(row=1, column=1, columnspan=2)
		tk.Label(text = "NEW LIST").grid(row=2, column=1)
		tk.Label(text = "LOAD LIST").grid(row=3, column=1)
		tk.Label(text = "DELETE LIST").grid(row=4, column=1)
		tk.Label(text = "EXIT").grid(row=5, column=1)
		
		self.text5 = tk.Label(textvariable = self.variable).grid(row=6, column=1)
		self.variable.set("a")

		self.button1 = tk.Button(text = "1.", command=lambda: self.tk_menu_option_1()).grid(row=2, column=0)
		self.button2 = tk.Button(text = "2.", command=lambda: self.tk_menu_option_2()).grid(row=3, column=0)
		self.button3 = tk.Button(text = "3.", command=lambda: self.tk_menu_option_3()).grid(row=4, column=0)
		self.button4 = tk.Button(text = "4.", command=lambda: self.tk_menu_option_4()).grid(row=5, column=0)
		
	def tk_menu_option_1(self):
		lw.main_option_1()
	
	def tk_menu_option_2(self):
		lw.main_option_2()

	def tk_menu_option_3(self):
		lw.main_option_3()
		
	def tk_menu_option_4(self):
		for widget in root.winfo_children():
			widget.destroy()
		tk.Label(text = "WARHAMMER 40K\n LIST BUILDER").grid(row=1, column=1, columnspan=2)
		tk.Label(text = "DO YOU WISH TO CLOSE THE PROGRAM?").grid(row=2, column=1)
		tk.Label(text = "WARNING: UNSAVED DATA WILL BE LOST").grid(row=3, column=1)

		self.button3 = tk.Button(text = "YES", command=lambda: sys.exit()).grid(row=4, column=1)
		self.button4 = tk.Button(text = "NO", command=lambda: self.return_to_main()).grid(row=5, column=1)
		
	def return_to_main(self):
		for widget in root.winfo_children():
			widget.destroy()		
		self.tk_main_menu()
		
root.title('WARHAMMER 40K LIST BUILDER')
root.minsize(150,50)
app = Application(master=root)
app.mainloop()