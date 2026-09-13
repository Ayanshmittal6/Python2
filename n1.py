def G_F():
    print("WELCOME TO THE SHOP")
G_F()
p_p_c = float(input("enter cost of 1 cup "))
p_c = int(input("enter no of cup sold "))
def c_t(p,c):
    total = p*c
    return total
t_c = c_t(p_p_c , p_c)
r_t = round(t_c,2)
print("total cost : ",r_t)
a_p = float(input("enter amount paid by custmor "))
def c_c(p,t):
    c = p - t
    return c
c_d = c_c(a_p, r_t)
print ("amount to pay back is : ", c_d)
print("thank you")