import random
message = "This is a secret message"
key = 6
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
		 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(noSpaces):
	#message = "This is a secret message"
	#noSpaces = removeSpaces(message)
	#print(noSpaces)
	n = len(noSpaces)
	encrypted_message = ''
	#key = 5
	#print(n/key)
	
	for j in range(0, key):
		for i in range(j, n, key):
			encrypted_message += noSpaces[i]
	print(encrypted_message)
	#decrypt(encrypted_message)


def removeSpaces(message):
	
	noSpaces = ""
	for letter in message:
		if letter != " ":
			noSpaces += letter
	return noSpaces

def addLetters(message):
	message = message
	for i in range(key - (len(message) % key)):
		x = random.choice(letters)
		message += x
	return message
	#print(message)

def decrypt(encrypted_message):
	
	n = len(encrypted_message)
	for key in range(1, int(n/2)):
		decrypted_message = ''
		for j in range(0, int(n / key)):
			for i in range(j, n, int(n / key)):
				decrypted_message += encrypted_message[i]
		print(decrypted_message)

def main(message):
	no_spaces = removeSpaces(message)
	
	if len(no_spaces) % key != 0:
		noSpaces_extended = addLetters(no_spaces)
		encrypt(noSpaces_extended)
	else:
		encrypt(no_spaces)
if __name__ == '__main__':
	main(message)

