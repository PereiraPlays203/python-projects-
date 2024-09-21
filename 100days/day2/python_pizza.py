print("welcome to python pizza!!")
size = input("what size pizza do you want ? s, m or l")
pepperoni = input("do you want a pepperoni in your pizza ? y or n")
cheese = input("do you want cheese in your pizza ? y or n")
price = 0

if size == "s":
    price += 15
elif size == "m":
    price += 20
elif size == "l":
    price += 25

if pepperoni == "y" :
    if size == "s":
        price += 2
    else:
        price += 3

if cheese == "y":
    price += 1

print(f"the total price of your pizza is: R${price}")