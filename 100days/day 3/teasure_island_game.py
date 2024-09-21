print("bem vindo a ilha do tesouro, onde suas escolhas tem consequencias")

choice1 = input("voce esta numa encruzilhada, deseja ir para a esquerda ou direita? ").lower()

if choice1 == "direita":
    choice2 = input("voce esta numa ilha "
                    "escreva espere para agurdar um barco "
                    "escreva nadar para sair nadando ").lower()
    if choice2 == "espere":
        choice3 = input("voce esta diante de 3 portas "
              "uma azul "
              "uma amarela "
              "uma vermelha "
              "qual voce escolhe? ").lower()
        if choice3 == "vermelha":
            print("esta sala esta pegando fogo, game over ")
        elif choice3 == "azul":
            print("esta sala está inundada, game over ")
        elif choice3 == "amarela":
            print("parabens a sala amarela continha o tesouro, final feliz :) ")
        else:
            print("voce nao selecionou uma porta válida, game over! ")
    else:
        print("voce foi atacado por um troll maluco, game over ")
        
else:
    print("voce caiu em um buraco, game over! ")
