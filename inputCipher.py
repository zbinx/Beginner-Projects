# Caesar Cipher encryption program

black = lambda text: '\033[0;30m' + text + '\033[0m'
red = lambda text: '\033[0;31m' + text + '\033[0m'
green = lambda text: '\033[0;32m' + text + '\033[0m'
yellow = lambda text: '\033[0;33m' + text + '\033[0m'

print(black("========================================================"))
intro = """
███████╗███████╗ ██████╗██████╗ ███████╗████████╗███████╗
██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝╚══███╔╝
███████╗█████╗  ██║     ██████╔╝█████╗     ██║     ███╔╝ 
╚════██║██╔══╝  ██║     ██╔══██╗██╔══╝     ██║    ███╔╝  
███████║███████╗╚██████╗██║  ██║███████╗   ██║   ███████╗
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝                                                     
"""
print(yellow(intro))
print(black("========================================================"))

print("\033[31;40mCipher MENU\033[m")
print("\n")
print(yellow("[1]")+green(" Encrypt msg"))
print(yellow("[2]")+green(" Decrypt msg"))
print(yellow("[3]")+green(" Exit Program"))

userChoice = int(input(yellow("Enter an option: ")))
print("\n")

# the string to be encrypted:
if userChoice == 1:
	message = input(("Enter msg to encrypt : "))
	key = input(("Enter the key to use (0-90) : "))
	key = int(key)
	mode = 'encrypt'
	SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]|;:<>,/'
	translated = ''

	for symbol in message:
		# Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
		if symbol in SYMBOLS:
			symbolIndex = SYMBOLS.find(symbol)
			translatedIndex = symbolIndex + key
			
			# Handle wraparound, if needed:
			if translatedIndex >= len(SYMBOLS):
				translatedIndex = translatedIndex - len(SYMBOLS)
			elif translatedIndex < 0:
				translatedIndex = translatedIndex + len(SYMBOLS)

			translated = translated + SYMBOLS[translatedIndex]

		else:
			# Append the symbol without encrypting/decrypting"
			translated = translated + symbol


if userChoice == 2:
	message = input(("Enter msg to Decrypt : "))
	key = input(("Enter the key to use (0-90) : "))
	key = int(key)
	mode = 'decrypt'
	SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]|;:<>,/'
	translated = ''

	for symbol in message:
		# Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
		if symbol in SYMBOLS:
			symbolIndex = SYMBOLS.find(symbol)
			translatedIndex = symbolIndex - key
			
			# Handle wraparound, if needed:
			if translatedIndex >= len(SYMBOLS):
				translatedIndex = translatedIndex - len(SYMBOLS)
			elif translatedIndex < 0:
				translatedIndex = translatedIndex + len(SYMBOLS)

			translated = translated + SYMBOLS[translatedIndex]

		else:
			# Append the symbol without encrypting/decrypting"
			translated = translated + symbol

if userChoice == 3:
	print("Exiting program. Goodbye!")
	exit()
# Output the translated string:

print(translated)
