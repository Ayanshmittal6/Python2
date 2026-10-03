# activity 1
try :
    n = int(input("enter a number = "))
    print(" you seiected ", n ,"good choice")
except ValueError as x :
    print("Exeption :", x)

# activity 2
try :
    n1 = int(input("enter a number = "))
    n2 = int(input("enter a number = "))
    r = n1 / n2
    print("Result is "r)
except ZeroDivisionError :
    print("Division by Zero is an Error!!")
except  ValueError:
    print("PLEASE ENTER THE THE VALID WHOLE NUMBERS")
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print("this will excecute")
# activity 3