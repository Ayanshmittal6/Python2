c = (input("enter / or **=")) 
if (c == "**"):
    x = int (input("enter number "))
    y = int(input("enter power "))
    a = 1
    for i in range (y):
        a=a*x
    print("output is", a)
else:
      x = int (input("enter number 1 "))
      y = int(input("enter number 2 "))
      sum = x/y
      print("output is ", sum)