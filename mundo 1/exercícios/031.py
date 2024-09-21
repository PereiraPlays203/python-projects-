print('Olá, viagens até 200km custam R$0,50 o km, acima é cbrad R$0,45 o km')
km = int(input('digite a kilometragem da sua viagem:'))
km1 = km * 0.50
km2 = km * 0.45
if km < 200:
    print("voce pagara R206", km1)
else:
    print("voce pagaraR$", km2)