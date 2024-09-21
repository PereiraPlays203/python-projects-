v = int(input('digite a velocidade do seu carro: '))
m1 = v - 80
m2 = m1 * 7

if v <= 80:
    print('Parabens!! você não tomou uma multa!!')
else:
    print(f'danadinho vc ein! vai toma uma multa de R${m2} conto!')