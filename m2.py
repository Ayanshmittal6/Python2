r = int(input("please enter nmuber row "))
n = 1
print("Float triange")
for i in range (1, r + 1):
    for j in range (1, i + 1):
        print(n, end = ' ')
        n = n + 1
    print(" ")