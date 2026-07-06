student = [{"ID": "101", "name": "Dron","Age": "20","Grade": "A",'''Date of Birth (yyyy-mm-dd)''': "1990-01-01","subjects": ["Math", "Science", "English"]},
           {"ID": "102", "name": "Deep","Age": "22","Grade": "B",'''Date of Birth (yyyy-mm-dd)''': "1988-05-15","subjects": ["Math", "Science", "English"]},
           {"ID": "103", "name": "vyom","Age": "21","Grade": "C",'''Date of Birth (yyyy-mm-dd)''': "1989-12-10","subjects": ["Math", "Science", "English"]},
]



print("Welcome to the Student Data Organizer!......")
print("select an option :")

print("1. Add a new student")
print("2. display all students")
print("3. Update student details")
print("4. Delete a student")
print("5. Display Subject offered")
print("6. Exit")
while True:
    choice = int(input("Enter your choice: "))
    if choice <1:
        print("Invalid choice. Please select a valid option.")
    elif choice >6:
        print("Invalid choice. Please select a valid option.")
    else:
        found = False
        if choice == 1:
            new_student = {}
            new_student["ID"] = input("Enter ID: ")
            new_student["name"] = input("Enter name: ")
            new_student["Age"] = input("Enter Age: ")
            new_student["Grade"] = input("Enter Grade: ")
            new_student["Date of Birth (yyyy-mm-dd)"] = input("Enter Date of Birth (yyyy-mm-dd): ")
            new_student["subjects"] = input("Enter subjects (comma-separated): ").split(",")
            
            student.append(new_student)
            found = True
            print("Student added successfully")
        if choice == 2: 
            print("--------------------------------------")
            for s in student:
                print(f"ID: {s["ID"]}, Name: {s["name"]},Age: {s["Age"]}, Grade: {s["Grade"]}, Date of Birth: {s['Date of Birth (yyyy-mm-dd)']},subject: {s["subjects"]}")
                found = True
            if not found:
                print("No students found.")
                break
            print("--------------------------------------")
            print("Student details displayed successfully")
        if choice == 3:
            print("--------------------------------------")
            updateID = input("Enter Student ID : ")
            for s in student:
                if s["ID"] == updateID:
                    s["name"] = input("Enter New Name : ")
                    s["marks"] = input("enter New Marks : ")
                    found = True
                    print("Student details updated successfully")
                    if not found:
                        print("Student not found.")
                        print("--------------------------------------")
        if choice == 4:
            print("--------------------------------------")
            DeleteID = input("Enter Student ID : ")
            for s in student:
                if s["ID"] == DeleteID:
                    student.remove(s)
                    found = True
                    print("Student deleted successfully")
                    if not found:
                        print("Student not found.")
                        print("--------------------------------------")
        if choice == 5:
            print("--------------------------------------")
            for s in student:
                print(f"{s["name"]}{s["subjects"]}")
                found = True
            if not found:
                print("No subjects found.")
            print("Subject details displayed successfully")
            print("--------------------------------------")
        if choice == 6:
            print("--------------------------------------")
            print("--------------------------------------")
            print("Exiting the program. Goodbye!")
            break
           

                    
                    

            
    
    

        

        