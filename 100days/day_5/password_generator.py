import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("gerador de senhas")
nr_letters= int(input("Quantas letras você gostaria de ter na sua senha ?\n")) 
nr_symbols = int(input(f"quantos símbolos você gostaria ?\n"))
nr_numbers = int(input(f"quantos números você gostaria ?\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
#print(password)

for sym in range(1,nr_symbols + 1):
    password_list += random.choice(symbols)
#print(password)

for num in range(1,nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(password)

