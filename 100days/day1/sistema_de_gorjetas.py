print("sistema de gorjetas")
conta = float(input("digite o valor da conta: "))
porcentagem_gorjeta = float(input("digite a porcentagem da gorjeta que gostaria de dar para o garçom: "))
pessoas = float(input("a conta será dividida em quantas pessoas ? "))
valor_gorjeta = float((porcentagem_gorjeta/100) * conta)
conta_dividida = round((conta+valor_gorjeta) / pessoas, 2)

print(f"cada pessoa deve pagar R${conta_dividida}")
