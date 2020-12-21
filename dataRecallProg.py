# Beginner python program that stores info in lists that can be called with various user input commands.
# Much like a chatroom bot that responds to command to spit out information.

import sys

print('Welcome to Users information system, please enter a list command to see a list of data.')

Nicks = (['Jonny5', 'Turbo1', 'Arkon', 'phobos', 'Parker Barnes']) # List of nicknames
Heros = (['JBP', 'Uncle Buck', 'Linus', 'Tesla'])                  # List of personal heros
Sites = (['Tryhackme', 'github', 'Code Academy'])				   # List of websites like to visit
Commands = (['nicks', 'heros', 'sites', 'commands'])      #The list of commands this program responds to


while True:

	userInput = input()

	if userInput == ('nicks'):
		print('Retreiving information:')
		print(*Nicks, sep = "\n")
		print('*********************************')
		print('Please enter another command:')

	
	
	elif userInput == ('sites'):
		print(*Sites, sep = "\n")
		print('*********************************')
		print('Please enter another command:')
	

	elif userInput == ('heros'):
		print(*Heros, sep = "\n")
		print('*********************************')
		print('Please enter another command:')	

	elif userInput == ('quit'):
		print('Program will exit now. Goodbye')
		print('*********************************')
		sys.exit()
		

	elif userInput == ('commands'):
		print(*Commands, sep = "\n")
		print('*********************************')
		print('Please enter another command:')

	else:
		userInput = input()
		continue


	

