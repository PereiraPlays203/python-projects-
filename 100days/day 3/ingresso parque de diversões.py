print("sistema do parque de diversões")
a = float(input("digite sua altura: "))
preco = 0
if a >= 1.20 :
    print("voce esta apto a andar na montanha russa")
    age = int(input("qual a sua idade ?"))
    if age <= 12:
        preco = 5
        print("a entrada para crianças custa R$5")
    elif age <=18:
        preco = 7
        print("a entrada para adolescentes custa é R$7")
    elif age >= 45 and age <= 55:
        preco = 0
    else:
        preco = 12
        print("a netrada para adultos éR$12 pelo ingresso")

    wants_photo = input("gostaria de uma foto durante o passeio por R$3 adicionais ? se sim digite y se não digite n")

    if wants_photo == "y":
        preco += 3
        print(f"você deve pagar R${preco}")
    else:
        print(f"voce deve pagar R${preco}")
else:
    print("você não pode andar na montanha russa!!")
