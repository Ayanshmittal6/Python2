ac=float(input("pls enter the actual product price"))
sa=float(input("pls enter the sale amount"))

if(sa>ac):
    amount=sa - ac
    print("total profit=",amount)
else:
    print("no profit!!!!")