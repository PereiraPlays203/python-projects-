weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi <= 18.5:
    print("você está abaixo do peso!")
elif bmi <= 24.9:
    print("voce está no peso normal!")
else:
    print("você está acima do peso!")
