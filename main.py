import random

password = str(input('Enter Password Noly Number : '))
guess = ' '

while guess != password:
	guess = str(random.randint(0,9999))
	print('> '+guess)
	if (guess == password):
		print('the password: '+password)
		break