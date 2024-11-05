quote = "I love python"
quote2 = "01234567890"
print(quote[0])
print(quote[1])

print(quote[3])
print(quote[4])
# [] index()

# Slice opetator
# quote[start:end] end is not included
print(quote[2:6])

print(quote[2:])

print(quote[2:10:3])
print(quote2[2:10:3])

print(quote[::-1])

print(quote[-10:-1:])

name = "  Shoki abc   "
print(name.upper()) # SHOKI ABC
print(name.lower())
print(name.strip())

# Task
secret_message = "   Programming in Python is not only powerful but also fun!   "

# Expected Output
# "PYTHON-POWERFUL"

upper_secret_msg = secret_message.upper()

print(upper_secret_msg[18:24] + "-" + upper_secret_msg[-25:-17])
print(upper_secret_msg[18:24], "-" ,upper_secret_msg[-25:-17])
print(f"{upper_secret_msg[18:24]}-{upper_secret_msg[-25:-17]}")

# Task 1.2
flipped_message = "!nuf sseldnE dna seitinutroppo lufrewop htiw nohtyP"

# Expected Output
# "python 🗡️ powerful 🌸"

revers_flipped_message = flipped_message[::-1]
revers_lower_flipped_message = revers_flipped_message.lower()
print(revers_flipped_message)
print(f"{revers_lower_flipped_message[0:6]} 🗡️  {revers_lower_flipped_message[12:20]} 🌸")

print(f"{revers_flipped_message[0:6].lower()} 🗡️  {revers_flipped_message[12:20].lower()} 🌸")

