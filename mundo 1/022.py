name = input('digite seu nome completo: ')
upper = name.upper()
lower = name.lower()
qname = name.split()

print(upper)
print(lower)
print(len(qname[0]))
print('seu nome completo tem {}'.format(len(name)-name.count(' ')))



