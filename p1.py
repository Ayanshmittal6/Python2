def c_c (pa,pr):
    c=pa-pr
    return c
s_p =25
print("=====SNACK'S VENDING MACHINE=====")
print(f"   THE SNACK COST IS {s_p} UNITS    ")
print("   Accepted coins = 1,5,10,25   ")
print("=================================\n")
 
total_inserted = 0
coins_inserted = 0
while True:
    coin = int(input("Insert a coin (1, 5, 10, or 25): "))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin, try again!\n")
        continue
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far: {total_inserted}\n")
 
    if total_inserted >= s_p:
        print("Enough money inserted!\n")
        break
change_due = c_c(total_inserted, s_p)
print("Printing your snack's bill")
if change_due == 0:
    pass
else:
    print(f"Here is your change: {change_due} units")
 
# PART 9: Print a short summary of the payment
print("\n===== PAYMENT SUMMARY =====")
print("snack Price:",s_p)
print("Coins Inserted:", coins_inserted)
print("Total Paid:", total_inserted)
print("Change Given:", change_due)
print("===========================")
print("your snack bill is complet!")
