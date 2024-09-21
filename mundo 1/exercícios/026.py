p = str(input('digite uma frase: ')).upper()

print(f'A letra A aparece {p.lower().count("a")} ')
print(f'aparece pela primeira vez na posição {p.find("A")}')
print(f'aparece pela última vez na posição {p.rfind("A")}')