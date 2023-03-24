# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""

for crat in range(1, nr_letters + 1):
    random_crat = random.choice(letters)
    #print(random_crat)
    password = password + random_crat
    print(password)

for sym in range(1, nr_symbols + 1):
    random_sym = random.choice(symbols)
    #print(random_crat)
    password = password + random_sym
    print(password)

for num in range(1, nr_numbers + 1):
    random_num = random.choice(numbers)
    #print(random_crat)
    password = password + random_num
    print(password)


print("========================================")
print("========================================")
print("========================================")


password_list = []

for crat in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for sym in range(1, nr_letters + 1):
    password_list += random.choice(symbols)

for num in range(1, nr_letters + 1):
    password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print((password_list))

password = ""
for crat in password_list:
    password += crat

print(f"Your password is: {password}") 