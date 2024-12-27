print("You need to pay 100$")
amount1=int(input("Enter how much $ you have payed:"))
amount2=100-amount1

if amount1==100:
    print("You have payed all the money you needed to pay")
else:
    print("You still need to pay",amount2,"$")