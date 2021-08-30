import math
message = "This is a secret message."
n = len(message)
key = 5
print(len(message))
print(math.ceil(n /key))



def encrypt():
	n = len(message)
	encrypted_message = ''
	key = 5
	print(int(n / key))
	for j in range(0, key):
		for i in range(0, n):
			if i % key == j:
				print(message[i], end='')
				encrypted_message += message[i]
	decrypt(encrypted_message)

	# for i in range(0, n):
	# 	if i % 4 == 1:
	# 		print(message[i], end='')
	# for i in range(0, n):
	# 	if i % 4 == 2:
	# 		print(message[i], end='')
	# for i in range(0, n):
	# 	if i % 4 == 3:
	# 		print(message[i], end='')
def decrypt(encrypted_message):
	n = len(encrypted_message)
	decrypted_message = ''
	if n % key == 0:
		while len(decrypted_message) < n:
			for j in range(0, int(n / key)):
				for i in range(j, n, math.ceil(n / key)):
					decrypted_message += encrypted_message[i]
		print(f"\n{decrypted_message}")
	elif n % key == 1:
		for j in range(0, int(n / key)):
			decrypted_message += encrypted_message[j]
			decrypted_message += encrypted_message[j + 7]
			decrypted_message += encrypted_message[j + 13]
			decrypted_message += encrypted_message[j + 19]
		decrypted_message += encrypted_message[int(n / key)]
			
		print(f"\n{decrypted_message}")


'''Only works if len(message) is divisible by key'''
# 	n = len(encrypted_message)
# 	for key in range(0, int(n)):
# 		for j in range(0, key):
# 			for i in range(0, n):
# 				if i % key == j:
# 					print(encrypted_message[i], end='')
# 		print('')

encrypt()
#decrypt('nalcxehwttdttfseeleedsoaxfeahl')