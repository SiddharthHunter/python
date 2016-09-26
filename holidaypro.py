print("Your choice of hotels")
print("1.Ipoh Bali Hotel")
print("2.Excelsior Hotel")
print("3.TheWolfGang Platinum Hotel")
print("Lost World Hotel")
print("1.Lost World Of Tambun")
print("2.Extreme Park(Sunway City)")
print("3.ATV Adventure")
print("You are on your way to Ipoh,start planning")
def hotels():
        ask = input("How do you want to travel")
        if ask == "bus":
                people = input("How many people")
        if people ==  1:
                print("The cost is $10")
        if people == 2:
                print("The cost is $20")
        if people == 3:
            print("The cost is $30")
        if people == 4:
            print("The cost is $40")
        if ask == "train":
                people = input("How many people")
        if people == 1:
                print("The cost is $10")
        if people == 2:
                print("The cost is $20")
        if people == 3:
                print("The cost is $30")
        if people == 4:
                print("The cost is $40")
        if ask == "plane":
                people = input("How many people")
        if people == 1:
            print("The cost is $59")
        if people == 2:
            print("The cost is $100")
        if people == 3:
            print("The cost is $150")
        if people == 4:
            print("The cost is $252")

choice = int(input("Choose A Hotel  :  "))
#ipoh bali
if choice == 1:
    story = int(input(" Which room : "))
    if story == 1:
           print("The price is $69.90")
    if story == 2:
        print("The price is $100.50")
    if story == 3:
        print("the price is $118.90")
    if story == 4:
        print("the price is $199.93")

#excelsior
    if choice == 2:
        moment = int(input("Which room : "))
        if moment == 1:
            print("The price is $69.90")
        if moment == 2:
            print("The price is $100.50")
        if moment == 3:
            print("The price is $118.90")
        if moment == 4:
            print("The price is $199.93")
    if choice == 3:
        tonight  = int(input("Which room : "))
        if tonight == 1:
            print("The price is $69.90")
        if tonight == 2:
            print("The price is $100.50")
        if tonight == 3:
            print("The price is $118.90")
        if tonight == 4:
            print("The price is $199.93")
    elif choice == 4:
        gone = int(input("Which room : "))
        if gone == 1:
            print("the price is $69.90")
        if gone == 2:
            print("the price is $100.50")
        if gone == 3:
            print("the price is $118.90")
        if gone == 4:
            print("the price is $199.93")
hotels()

def enjoy():
        print("Enjoy your trip")
        distance = input("Choose your own attraction")
        
        
enjoy()
