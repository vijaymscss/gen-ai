students = [
    # {"name": "Arun", "marks": 85}
]



def get_grade(marks):
    if (marks >= 90 and marks <= 100):
        return "A"
    elif (marks >= 80 and marks <= 89):
        return "B"
    elif (marks >= 70 and marks <= 79):
        return "C"
    elif (marks >= 60 and marks <= 69):
        return "D"
    elif (marks < 60):
        return "E"


def show_results():
    
    average=0
    highest=0
    lowest=0
    totalMarks = 0
    
    
    if(len(students)==0):
        print("No students")
        return
    

    print("\n\n=====Student marklist=====")
    print(f"{'Name':<15} {'Marks':<10} {'Grade':<10}")
    
    for student in students:
        grade = get_grade(student["marks"])
        print(
            f"{student['name']:<15} "
            f"{student['marks']:<10} "
            f"{grade:<10} "
        )
        
        if(student["marks"]>highest):
            highest = student["marks"]

        if(student["marks"]<lowest):
            lowest = student["marks"]
            
        totalMarks += student["marks"]
            
        
    print("\n\n======Summary======")
    print(f"Average marks: {totalMarks / len(students)}")
    print(f"Highest marks: {highest}")
    print(f"Lowest marks: {lowest}")
    
    
def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty")
        return

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student already exists")
            return

    try:
        marks = int(input("Enter student marks: "))
    except ValueError:
        print("Invalid marks")
        return

    if marks < 0 or marks > 100:
        print("Invalid marks")
        return

    students.append({"name": name, "marks": marks})
    print("Student added successfully")
    
        
        
while(True):
    print(f"\n\n=======Menu=======")
    print(f"1.Display Student Details")
    print(f"2.Add Student Details")
    print(f"3.Exit")   

    choice = input("Enter your choice: ")
    if(choice == "1"):
        show_results()
    elif(choice == "2"):
        add_student()
    elif(choice == "3"):
        break
    else:
        print("Invalid choice")
        
    