print("Enter Marks")
m1=int(input())
m2=int(input())
m3=int(input())
total=m1+m2+m3
avg=int(total/3)
validrange = range(0,101)
if avg not in validrange:
     print("invalid input")
elif avg in range(81, 101):
     print("A GRADE")
elif avg in range(61, 81):
     print("B GRADE")
elif avg in range(41, 61):
     print("C GRADE")
elif avg in range(21, 41):
     print("D GRADE")
else:
     print("SORRY YOU GRADE IS LOW")