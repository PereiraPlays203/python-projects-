c = str(input('digite o nome da sua cidade: '))
cl = c.split()
print(f'o nome da sua cidade é {c} e o primeiro nome é {cl[0]} e se começa com santos {c.upper()[0:6] == "SANTOS"}')
