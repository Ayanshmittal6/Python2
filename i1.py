print("======================")
print("WELCOME TO RIDE BILDER")
print("======================")
print()

print("STEP 1 : SELECT YOUR VEHICEL")
print("1= BIKE")
print("2=CAR")
print()

choice = int(input("type 1 or 2"))
print()

if choice == 1:
    print("PICK YOUR BIKE TYPE")
    print("1=SCOOTY")
    print("2=MOUNTAIN BIKE")

    pant = int(input("type 1 or 2"))
    print()
    
    if pant == 1:
        print("=================")
        print("YOU CHOICE : SCOOTER")
        print("TOP SPEED : 80 Km")
        print("BEST FOR : CITY ROAD")
        print("=================")
    else:
            print("=================")
            print("YOU CHOICE : MOUNTAIN BIKE")
            print("TOP SPEED : 40 Km")
            print("BEST FOR : OFF-ROAD TRACK")
            print("=================")
elif choice == 2:
    print("PICK YOUR CAR TYPE")
    print("1=SEDAN")
    print("2=SUV")

    pant = int(input("type 1 or 2"))
    print()
    
    if pant == 1:
        print("=================")
        print("YOU CHOICE : SEDAN")
        print("SEATS : 5 SEATS")
        print("BEST FOR : FAMILY TRIP")
        print("=================")
    else:
            print("=================")
            print("YOU CHOICE : SUV")
            print("SEATS : 7 SEATS")
            print("BEST FOR : OFF-ROAD ADVENCHER")
            print("=================")
else:
     print("THAT IS NO A OPTION")
     print(" PEASE TRY AGAIN")
print("")
print("====================")
print("THANK YOU COME AGAIN")
print("====================")