import random
import ascii
#0 == pedra
#1 == papel
#2 == tesoura
list = [0,1,2]

cpu = random.choice(list)

user = int(input("Digite 0 para pedra, 1 para papel e 2 para tesoura: "))

#bloco para mostrar o que o usuario escolheu
if user == 0:
    print(ascii.rock)
elif user == 1:
    print(ascii.paper)
else:
    print(ascii.scisors)
#bloco para mostrar o que o usuario escolheu

print("O computador escolheu: ")

#bloco para mostrar o resultado do pc
if cpu == 0:
    print(ascii.rock)
elif cpu == 1:
    print(ascii.paper)
else:
    print(ascii.scisors)
#bloco para mostrar o resultado do pc

if user == 0 and cpu == 2:
    print("VITÓRIA!")
elif user == 0 and cpu == 1:
    print("DERROTA!")
elif user == 0 and cpu == 0:
    print("EMPATE!")

if user == 1 and cpu == 2:
    print("DERROTA!")
elif user == 1 and cpu == 1:
    print("EMPATE!")
elif user == 1 and cpu == 0:
    print("VITÓRIA!")

if user == 2 and cpu == 2:
    print("EMPATE!")
elif user == 2 and cpu == 1:
    print("VITÓRIA!")
elif user == 2 and cpu == 0:
    print("DERROTA!")




