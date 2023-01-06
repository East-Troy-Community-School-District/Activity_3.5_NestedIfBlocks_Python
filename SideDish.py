'''
Side Dish
1/6//2023
Python I

Instructions:
Run the program and try entering a variety of side
dishes. What happens? Why? When did you get asked
about ketchup? Why does it only happen for that
side dish? In your own words, describe how nested
if statements work.
'''

side = input("Do you want fries, onion rings, or cheese curds? >> ")
if side == "fries":
    ketchup = input("Do you need ketchup? (yes/no) >> ")
    if ketchup == "yes":
        print("Fries with k-up coming up!")
    else:
        print("Fries hold the k-up!")
elif side == "onion rings":
    print("Tossing onion rings your way!")
elif side == "cheese curds":
    print("You must be from Wisconsin!")
else:
    print("No side for you!")
