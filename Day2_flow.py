# Read from the User
fav_flavour = input("What can I for you ?")  

# Shop
stock1 = "chocolate mint"
stock2 = "vanilla"
stock3 = "coffee"
stock4 = "green tea"

# Expected Output
# Yes, we have vanilla in stock

# Sorry, we ran out strawberry

fav_flavour_lower = fav_flavour.lower()

# if fav_flavour_lower == stock1:
#     print(f"Yes, we have {fav_flavour_lower} in stock")
# elif fav_flavour_lower == stock2:
#     print(f"Yes, we have {fav_flavour_lower} in stock")
# elif fav_flavour_lower == stock3:
#     print(f"Yes, we have {fav_flavour_lower} in stock")
# elif fav_flavour_lower == stock4:
#     print(f"Yes, we have {fav_flavour_lower} in stock")
# else:
#     print(f"Sorry, we ran out {fav_flavour_lower}")


# if fav_flavour_lower == stock1 or fav_flavour_lower == stock2 or fav_flavour_lower == stock3 or fav_flavour_lower == stock4:
#     print(f"Yes, we have {fav_flavour_lower} in stock")
# else:
#     print(f"Sorry, we ran out {fav_flavour_lower}")

if fav_flavour_lower in [stock1, stock2, stock3, stock4]:
    print(f"Yes, we have {fav_flavour_lower} in stock")
else:
    print(f"Sorry, we ran out {fav_flavour_lower}")

