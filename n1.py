print ("lets print some shaps")
print("Star Piramad Pattern")
n = int(input("enter the number of rows"))
for i in range (n):
    for j in range (i+1):
        print("*",end = " ")
    print(" ")
print("Float triange") 
r = int(input("please enter nmuber row "))
n = 1
for i in range (1, r + 1):
    for j in range (1, i + 1):
        print(n, end = ' ')
        n = n + 1
    print(" ")
print("Diamond Number Pattern")
r = int(input("enter number of : "))
if r %2 == 0:
    h =int(r/2)
else:
    h =int(r/2)+1
s = h-1
for i in range (1,h+1):
    for j in range (1,s+1):
        print(end=" ")
    s = s - 1
    n = 1
    for j in range (2*i-1):
        print(end=str(n))
        n = n+1
    print("")
s = 1
for i in range (1,h+1):
    for j in range (1,h+1):
        print(end=" ")
    s = s + 1
    n = 1
    for j in range (1,2*(h-i)):
        print(end=str(n))
        n = n+1
    print("")