'''
Cinthya Calderon-Hernandez
CSMC111
Spring 2026
Reading CSC File with Error Handling
'''

#Used ChaptGPT
import csv

filename = input("Enter CSV file name: ")

valid_data = []

try:
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        print("\nProcessing data...\n")

        for row_num, row in enumerate(reader, start=1):

            try:
                name = row.get("name", "").strip()
                age = row.get("age", "").strip()
                grade = row.get("grade", "").strip()

                # Check missing values
                if not name:
                    print(f"Row {row_num}: Missing name → skipped")
                    continue

                if not age:
                    print(f"Invalid record for {name}: missing age")
                    continue

                if not grade:
                    print(f"Invalid record for {name}: missing grade")
                    continue

                # Convert values
                age = int(age)
                grade = int(grade)

                # Store valid data
                valid_data.append({
                    "name": name,
                    "age": age,
                    "grade": grade
                })

                print(f"Valid record: {name} (Age: {age}, Grade: {grade})")

            except ValueError:
                print(f"Invalid record for {name}: age or grade is not a number")
                continue

    print("\nFinished processing.\n")

except FileNotFoundError:
    print("File not found!")

except Exception as e:
    print("An unexpected error occurred.")
    print(f"Details: {e}")