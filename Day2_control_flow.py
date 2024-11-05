
x = 1
y = 2

if x > y:
    print(f"{x} is greater")
else:
    print(f"{y} is greater")


# Task
# Get two person name
# Case 1:
# Yuma, Yoshi
# 173cm, 163cm
# Expected
# Yuma is taller than Yoshi by 10cm

# Case 2:
# Yuma, Yoshi
# 173cm, 185cm
# Expected
# Yoshi is taller than Yuma by 12cm

# user1_name = input("user1 name please ")
# user1_height = float(input(f"{user1_name} height "))
# user2_name = input("user2 name please ")
# user2_height = float(input(f"{user1_name}  height "))


# if user1_height > user2_height:
#     print(f"{user1_name} is taller than {user2_name} by {user1_height - user2_height}cm")
# elif user1_height == user2_height:
#     print(f"{user1_name} and {user2_name} is same height")    
# else:
#     print(f"{user2_name} is taller than {user1_name} by {user2_height - user1_height}cm")


user1_name = input("user1 name please ")
user1_height = float(input(f"{user1_name} height "))
user2_name = input("user2 name please ")
user2_height = float(input(f"{user1_name}  height "))
diff_height = abs(user1_height - user2_height)

if user1_height > user2_height:
    print(f"{user1_name} is taller than {user2_name} by {diff_height}cm")
elif user1_height == user2_height:
    print(f"{user1_name} and {user2_name} is same height")    
else:
    print(f"{user2_name} is taller than {user1_name} by {diff_height}cm")


