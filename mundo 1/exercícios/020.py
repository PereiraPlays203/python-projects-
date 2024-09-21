from random import shuffle
a1 = input('digite o 1 corno: ')
a2 = input('digite o 2 corno: ')
a3 = input('digite o 3 corno: ')

lis = [a1,a2,a3]
print(f'a ordem do mais corno é {shuffle(lis)}')