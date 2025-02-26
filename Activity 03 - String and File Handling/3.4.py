try:
    with open("students.txt", "r") as file:
        student_data = file.readlines()

    print("Reading Student Information:")
    for line in student_data:
        print("   " + line.strip())

except FileNotFoundError:
    print("Error: The file 'students.txt' was not found.")