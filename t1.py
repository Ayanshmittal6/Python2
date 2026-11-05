# lesson 1
tuplex1 = ("tuple",False,32,1)
print(tuplex1)
tuplex2 = (4,6,2,8,3,1)
print(tuplex2)
tuplex3 = (50,10,60,70,50)
print(tuplex3)
tuplex4 = (2,4,3,5,4,6,7,8,6,1)
print(tuplex4[3:5])
print(tuplex4[:6])
#lesson2
def paline(r):
    e = len(r)-1
    s = 0
    while (s<e):
        if(r[s]!=r[e]):
            return False
        s+=1
        e-=1
    return True
r = (1,2,3,3,2,1)
if(paline(r)):
    print("Tuple is  Flip-flop")
else:
    print("Tuple is not Flip-flop")