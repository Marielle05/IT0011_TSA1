first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name

print("\nFull Name:", full_name)
print("Full Name (Upper Case):", full_name.upper())
print("Full Name (Lower Case):", full_name.lower())

name_length = len(full_name.replace(" ", ""))
print("Length of Full Name:", name_length)
