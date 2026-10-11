import random
p = True
n = random.randint(0,9)
print("")
print("    guess the number    ")
print("")
while p :
    no = int(input("enter a random number"))
    if  no == n:
        print("")
        print("    you win   ")
        break
    else:
        print("try again")