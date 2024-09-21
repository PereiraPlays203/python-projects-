dias = int(input('digite a quantidade de dias em que o carro foi alugado:'))
km = float(input('digite a quantidade de km rodados:'))
p = (0.15*km)+dias*60
print(f'o preço a pagar é {p}')
