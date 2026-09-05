print("==========================")
print("Welcome to billing counter")
print("==========================")
print("")

print("===========================")
print("        First Step")
a = int(input("Enter number of things: "))
print("===========================")
print("")

sum=0
print("===========================")
print("       Second Step")
for i in range(a):
    b = int(input("Enter 1 or 2(1= drink, 2= food): "))
    if(b == 1):
        sum = sum + 20
    else:
        sum = sum + 50

print("=====================================")
print("Calculting the amount you have to pay")
print("=====================================")
print("Please Pay Rs. ",sum)


