#Mini project - 6
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

User_letters = int(input("How many letters do you require? \n"))
User_numbers = int(input("How many numbers do you require? \n"))
User_symbols = int(input("How many symbols do you require? \n"))

#structured password
# password = "" 
# for char in range(0, User_letters):
#     password += random.choice(letters)

# for char in range(0, User_numbers):
#     password += random.choice(numbers)

# for char in range(0, User_symbols):
#     password += random.choice(symbols)

# print(password)

#unstructured password
password = []
for char in range(0, User_letters):
     password.append(random.choice(letters))

for char in range(0, User_numbers):
     password.append(random.choice(numbers))

for char in range(0, User_symbols):
      password.append(random.choice(symbols))

random.shuffle(password)
password_final = ""

for char in password:
     password_final += char

print(password_final)