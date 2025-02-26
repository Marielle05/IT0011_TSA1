last_name = input("Enter last name: ")
first_name = input("Enter first name: ")
age = input("Enter age: ")
contact_number = input("Enter contact number: ")
course = input("Enter course: ")

with open("students.txt", "a") as file:
    file.write(f"First Name: {first_name}\n")
    file.write(f"Last Name: {last_name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Contact Number: {contact_number}\n")
    file.write(f"Course: {course}\n")
    file.write("-" * 30 + "\n")

print("Student information has been saved to 'students.txt'.")