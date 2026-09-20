#activity 1
def t_b(b,t):
    to = b*(1+0.01*t)
    to= round(to,2)
    print("Total amont to give :",to)
t_b(150,20)


#activity 2
def c(n):
    return n*n*n
def b_3 (n):
    if n%3==0:
        return(c (n))
    else:
        return False
print(b_3(9))
print(b_3(4))


#activity 3
def f (n):
    '''this is recursive function'''
    if n==0 or n==1:
        return 1
    else:
        return n*f(n-1)
print(f,__doc__)
print("the factorial of 0 : ",f(0))
print("the factorial of 1 : ",f(1))
print("the factorial of 2 : ",f(2))
print("the factorial of 3 : ",f(3))
print("the factorial of 4 : ",f(4))
print("the factorial of 5 : ",f(5))