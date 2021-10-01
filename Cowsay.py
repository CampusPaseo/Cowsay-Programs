# This Program Was Created On October 1st at 11:27 AM
# Using Python3 Programming Language
# Okay Good Luck and Have a Nice Day :)

# Create a Function To Create "about program author".
def about_programs_author():
	print("""\033[1m
		+===========================================================================+
		.................... FSOCIETY HACKER SYNDICATE ....................
		+===========================================================================+
			[!] Author          : BenLeo Cyber Security
			[!] Team            : fSociety Hacker Syndicate
			[!] Created         : October 1, 2021 at 11:38 AM
			[!] GitHub          : https://github.com/CampusPaseo/
			[!] Defacer ID      : https://defacer.id/archive/team/fsociety-hacker
		+===========================================================================+
		""")


# Create Python3 Color Code
def python3_color_code():
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
python3_color_code()


# Clean Screen
import os, sys
os.system("clear")


# Make The Cowsay Programs
def cowsay_programs():
	import os
	import sys
	import datetime
	import cowsay
	# There are Various Types of COWSAY, here I will make them one by one, according to the type.
	#############################################################################################
	cowsay.beavis("\033[1mHi, fSociety Hacker Syndicate Was Here")
	# Diterjemahkan dari bahasa Inggris-Beavis adalah karakter fiksi 
	# Yang berperan sebagai salah satu dari dua protagonis remaja dari serial animasi MTV Beavis dan Butt-Head. 
	# Dia disuarakan oleh pencipta acara, Mike Judge.
	############################################################################################################
	cowsay.cheese("Hi, fSociety Hacker Syndicate Was Here")
	# Cheese = Keju Yummy Yummy :3

	cowsay.cow("Hi, fSociety Hacker Syndicate Was Here")
	# Cow = Sapi
cowsay_programs()


# The big program or the core of all cowsay programs is here
def The_big_program_or_the_core_of_all_cowsay_programs_is_here():
	import os, sys, cowsay
	cowsay.beavis("\033[1mHi, fSociety Hacker Syndicate Was Here")
	cowsay.cheese("Hi, fSociety Hacker Syndicate Was Here")
	cowsay.cow("Hi, fSociety Hacker Syndicate Was Here")
	cowsay.daemon("Hi, fSociety Hacker Syndicate Was Here")
	cowsay.dragon("Hi, fSociety Hacker Syndicate Was Here")
	cowsay.ghostbusters("Hi, fSociety Hacker Syndicate Was Here")
	cowsay.kitty("Hi, fSociety Hacker Syndicate Was Here")
	cowsay.meow("Hi, fSociety Hacker Syndicate Was Here")
	cowsay.milk("Hi, fSociety Hacker Syndicate Was Here")
	cowsay.pig("Hi, fSociety Hacker Syndicate Was Here")
	cowsay.stegosaurus("Hi, fSociety Hacker Syndicate Was Here")
	cowsay.trex("Hi, fSociety Hacker Syndicate Was Here")
	cowsay.stimpy("Hi, fSociety Hacker Syndicate Was Here")
	cowsay.turtle("Hi, fSociety Hacker Syndicate Was Here")
The_big_program_or_the_core_of_all_cowsay_programs_is_here()


def about_program_writer():
	import datetime, time
	from time import sleep
	from datetime import date
	from calendar import calendar

	# Get time now
	localtime = time.asctime(time.localtime(time.time()))
	print("[!] Localtime Now Is " + str(localtime))
	print("""\033[1m
		+===========================================================================+
		........................ FSOCIETY HACKER SYNDICATE ..........................
		+===========================================================================+
		[!] Author          : BenLeo Cyber Security
		[!] Team            : fSociety Hacker Syndicate
		[!] Created         : October 1, 2021 at 11:38 AM
		[!] GitHub          : https://github.com/CampusPaseo/
		[!] Defacer ID      : https://defacer.id/archive/team/fsociety-hacker
		+===========================================================================+
		""")
about_program_writer()

def make_a_calendar():
	import calendar
	# Make a calendar using python
	year = 2021
	month = 10
	print(calendar.month(year, month))
make_a_calendar()