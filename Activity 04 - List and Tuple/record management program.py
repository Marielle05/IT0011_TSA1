import json
import os

def compute_final_grade(class_standing, major_exam):
    return (0.6 * class_standing) + (0.4 * major_exam)

def load_records(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                data = file.read()
                return json.loads(data) if data else []
            except json.JSONDecodeError:
                print("Error: File is corrupted or not in valid JSON format.")
                return []
    return []

def save_records(filename, records):
    with open(filename, 'w') as file:
        json.dump(records, file, indent=4)

def save_records_text(filename, records):
    with open(filename, 'w') as file:
        for record in records:
            final_grade = compute_final_grade(record['class_standing'], record['major_exam'])
            file.write(f"ID: {record['id']}, Name: {record['name'][0]} {record['name'][1]}, Class Standing: {record['class_standing']}, Major Exam: {record['major_exam']}, Final Grade: {final_grade:.2f}\n")

def show_all_students(records, order_by='last_name'):
    if not records:
        print("No student records available.")
        return
    
    if order_by == 'last_name':
        records.sort(key=lambda x: x['name'][1].lower())
    elif order_by == 'grade':
        records.sort(key=lambda x: compute_final_grade(x['class_standing'], x['major_exam']), reverse=True)
    
    for record in records:
        final_grade = compute_final_grade(record['class_standing'], record['major_exam'])
        print(f"ID: {record['id']}, Name: {record['name'][0]} {record['name'][1]}, Final Grade: {final_grade:.2f}")

def show_student(records, student_id):
    if not records:
        print("No student records available.")
        return
    
    for record in records:
        if record['id'] == student_id:
            print(f"ID: {record['id']}, Name: {record['name'][0]} {record['name'][1]}, Class Standing: {record['class_standing']}, Major Exam: {record['major_exam']}, Final Grade: {compute_final_grade(record['class_standing'], record['major_exam']):.2f}")
            return
    print("Student not found.")

def add_record(records):
    student_id = input("Enter Student ID (6-digit): ")
    if not student_id.isdigit() or len(student_id) != 6:
        print("Invalid ID format.")
        return
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    try:
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam = float(input("Enter Major Exam Grade: "))
    except ValueError:
        print("Invalid grade input.")
        return
    records.append({"id": student_id, "name": (first_name, last_name), "class_standing": class_standing, "major_exam": major_exam})

def edit_record(records, student_id):
    if not records:
        print("No student records available.")
        return
    
    for record in records:
        if record['id'] == student_id:
            try:
                record['class_standing'] = float(input("Enter new Class Standing Grade: "))
                record['major_exam'] = float(input("Enter new Major Exam Grade: "))
            except ValueError:
                print("Invalid grade input.")
            return
    print("Student not found.")

def delete_record(records, student_id):
    if not records:
        print("No student records available.")
        return
    
    for i, record in enumerate(records):
        if record['id'] == student_id:
            del records[i]
            print("Record deleted.")
            return
    print("Student not found.")

def main():
    records = []
    filename = "students.json"
    
    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Show Student Record")
        print("6. Add Record")
        print("7. Edit Record")
        print("8. Delete Record")
        print("9. Exit")
        
        choice = input("Enter choice: ")
        if choice == '1':
            records = load_records(filename)
            print("File loaded.")
        elif choice == '2':
            save_records(filename, records)
            print("File saved.")
        elif choice == '3':
            filename = input("Enter new filename: ")
            save_records_text(filename, records)
            print("File saved as text format.")
        elif choice == '4':
            order = input("Order by (last_name/grade): ").strip().lower()
            if order in ['last_name', 'grade']:
                show_all_students(records, order_by=order)
            else:
                print("Invalid order choice.")
        elif choice == '5':
            student_id = input("Enter Student ID: ")
            show_student(records, student_id)
        elif choice == '6':
            add_record(records)
        elif choice == '7':
            student_id = input("Enter Student ID to edit: ")
            edit_record(records, student_id)
        elif choice == '8':
            student_id = input("Enter Student ID to delete: ")
            delete_record(records, student_id)
        elif choice == '9':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()