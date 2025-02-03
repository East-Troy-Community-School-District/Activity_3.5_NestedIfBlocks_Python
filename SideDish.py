'''
Side Dish
Pawelski
2/2/2025

Instructions:
1.  Run the program and try entering a variety of side
    dishes.
2.  When did you get asked about ketchup? Why does it only
    happen for that side dish?
3.  How do nested if blocks work?
4.  Modify the program so that it asks the user if they
    would like ranch when they order onion rings.
5.  Modify the program so that it asks the user if they
    would like cheese sauce when they order cheese curds.
6.  Modify the program by adding mozzarella sticks as a side
    dish. When the user orders mozzarella sticks, the program
    should ask whether the user wants marinara sauce.
'''

side = input("Do you want fries, onion rings, or cheese curds? >> ")
if side == "fries":
    ketchup = input("Do you need ketchup? (yes/no) >> ")
    if ketchup == "yes":
        print("French fries with ketchuo added to your order.")
    else:
        print("French fries added to your order.")
elif side == "onion rings":
    print("Onion rings added to your order.")
elif side == "cheese curds":
    print("Cheese curds added to your order.")
else:
    print("No side was added to your order.")
