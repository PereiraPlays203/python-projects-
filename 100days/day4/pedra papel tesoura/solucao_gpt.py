import random

# Escolhas do jogo
choices = [0, 1, 2]

# Resultados ASCII para as escolhas
rock = '''
  _______
-----'   ____)
      (_____)
      (_____)
      (____)
-----._(___)
'''

paper = '''
  _______
-----'   ____)____
          ______)
          _______)
         _______)
-----._(___)
'''

scissors = '''
  _______
-----'   ____)____
      (_____)
-----._(___)
'''

# Escolha do computador
cpu = random.choice(choices)

# Entrada do usuário
try:
    user = int(input("Digite 0 para pedra, 1 para papel e 2 para tesoura: "))
    if user not in choices:
        raise ValueError("Escolha inválida!")

    # Mostrar escolha do usuário
    if user == 0:
        print(rock)
    elif user == 1:
        print(paper)
    else:
        print(scissors)

    # Mostrar escolha do computador
    print("O computador escolheu: ")
    if cpu == 0:
        print(rock)
    elif cpu == 1:
        print(paper)
    else:
        print(scissors)

    # Determinar e mostrar o resultado
    if user == cpu:
        print("EMPATE!")
    elif (user == 0 and cpu == 2) or (user == 1 and cpu == 0) or (user == 2 and cpu == 1):
        print("VITÓRIA!")
    else:
        print("DERROTA!")

except ValueError as e:
    print(e)