first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")

full_name = first_name + " " + last_name
print("\nFull Name:", full_name)

sliced_name = first_name[:4]
print("Sliced Name:", sliced_name)

greeting_message = f"Greeting Message: Hello, {sliced_name}! Welcome. You are {age} years old."
print(greeting_message)