# Exercise 8d: Create a student manager using a dictionary.
# Each student has an ID (key), and a value with a name and list of grades.
# After data entry, show all students, and print the average grade of one selected student.

def student_manager():
    # ↓↓↓ Write your code here ↓↓↓
    exit = False
    students = {}
    while exit == False:
        print_menu()
        option = (input("Select an option from the menu: "))
        match option:
            case "1":
                students[f"stu{len(students)}"] = add_student() #{name : "name", grades : "grades"}
                print(f"Student correctly added with the following information: {students[f"stu{len(students)-1}"]}")
            case "2":
                search_student(students)
            case "3":
                display_all_students(students)
            case "4":
                update_student(students)
            case "5":
                run_calc_average(students)
            case _:
                print(f"-"*50)
                print("Not a valid option:")
                
            
                

            
            
            
    # ↑↑↑ Write your code here ↑↑↑

def print_menu():
    print("-" * 20 + "MENU" + "-" * 20)
    print("1-Add new student")
    print("2-Search student")
    print("3-Display all students")
    print("4-Update student information")
    print("5-Calculate average from student")
    print("5-Delete student")
    print("_" * 50)

def add_student():
    name = input("Enter student´s name: ")
    grades = []
    exit = False
    option = ""
    while exit == False:
        option = ""
        print("_" * 50)
        grades.append(input(f"Entering {name}'s grade {len(grades) + 1}º: "))
        print(f"Grade {len(grades)} correctly registered with a value of: {grades[len(grades)-1]}")
        while option.lower() == "" or option.lower() != "y" and option.lower() != "n":
            option = input("Do you want to add another grade(y) or do you want to complete the registration(n) (n/y):")
            if option.lower() == "y":
                exit = False
            elif option.lower() == "n":
                exit = True
            else:
                print("Not a correct option, try again")
            print("_" * 50)
    return {"name" : name, "grades" : grades}

def search_student(students):
    search = input("Input search parameter(id or name): ")
    search_result = None
    print(students['stu0'])
    for i in range(len(students)):
        key = f"stu{i}"
        if search.lower() == key.lower() or search.lower() == students[f"{key}"]["name"].lower():
            print("_" * 50)
            print(f"Studen found: {students[key]["name"]}")
            print(f"With the following grades: {students[key]["grades"]}")
            print("_" * 50)
            search_result = students[f"{key}"]
            return search_result
        else:
            print(f"No student found with those seach parameters")
    
def display_all_students(students):
    print(f"Printing all students from a total of {len(students)}: ")
    for key, student in students.items():
        print(f"-" * 50)
        print(f"Student {key} with name: {student["name"]}")
        print(f"And the following grades: {student["grades"]}")
        
def update_student(students):
    selection = input(f"Select an student to update by name or id: ")
    i = 0
    option = ""
    for key, student in students.items():
        i += 1
        if selection.lower == key.lower() or selection.lower() == student["name"].lower():
            i = 0
            while option.lower() != "n" and option.lower() != "g": 
                option = input(f"Do you want to edit name or grades n/g: ")
                if option == "g":
                    print(f"Current grades: {student["grades"]}")
                    grade_position = int(input("What grade do you whant to update, select by possition number starting from 0: "))
                    student["grades"][grade_position] = input(f"Enter new grade: ")
                    print(f"*"*50)
                    print(f"Grade in position: {grade_position} succesfully modified with new grade value: {student["grades"][grade_position]}")
                    print(f"*"*50)
                    #exit = True
                elif option == "n":
                    new_name = input(f"Enter new name to replace ({student["name"]}): ")
                    student["name"] = new_name
                    print(f"*"*50)
                    print("Name succesfully changed!")
                    print(f"New name: {student["name"]}")
                    print(f"*"*50)
                    #exit = True
                else:
                    print("Not a valid option!")
        elif i >= len(students):
            print("No math found for that!")
    
def run_calc_average(students):
    selection = input("Select the student you want to find the average grade (by name or id): ")
    for key, student in students.items():
        if selection.lower() == student["name"].lower() or selection.lower() == key.lower():
            average = calc_average(student["grades"])
            print(f"The average grade for {student["name"]} is: {average}")
        else:
            print("Cannot find a match for that student!")
             
def calc_average(grades):
    t = 0
    average = 0
    for grade in grades:
        t += float(grade)
    average = t/len(grades)
    print(t)
    print(average)
    return average
        
        
    
    
    
# --- DO NOT EDIT BELOW THIS LINE ---
def run_test():
    print("Example: 2 students entered")
    print("stu01: Alice with grades [9.0, 8.5]")
    print("stu02: Bob with grades [6.0, 7.5, 8.0]")
    print("User selects stu02 → Output: average is 7.17")
    print("--- Now it's your turn ---")
    student_manager()

if __name__ == "__main__":
    run_test()
