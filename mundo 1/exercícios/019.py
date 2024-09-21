import random

a1 = input('digite o nome do 1 bicha: ')
a2 = input('digite o nome do 2 bicha: ')
a3 = input('digite o nome do 3 bicha: ')

lis = [a1,a2,a3]

print(f'o mais corno é o {random.choice(lis)}')