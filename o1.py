def G_F():
    print("WELCOME TO ART SUPPLIES STORE")
G_F()
p_p_c = float(input("enter cost of 1 per art item"))
p_c = int(input("enter no of art items sold "))
def c_t(p,c):
    total = p*c
    return total
t_c = c_t(p_p_c , p_c)
r_t = round(t_c,2)
a_p = float(input("enter amount paid by custmor "))
def c_c(p,t):
    c = p - t
    return c
c_d = c_c(a_p, r_t)
print("======================")
print("total cost : ",r_t)
print ("art items sold ", p_c)
print ("amount paid by custmor ", a_p)
print ("amount to pay back is : ", c_d)
print("======================")
print("thank you")