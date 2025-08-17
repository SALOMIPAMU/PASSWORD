import random
print("Welcome to your password generator")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"
number= input('Amount of password generations:')
number=int(number)
length = input('Input your password length:')
length=int(length)
print('\n here are your passwords:')
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
