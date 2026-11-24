employees = [
    {"id": 101, "name": "Arun", "department": "IT", "salary": 45000},
    {"id": 102, "name": "Bala", "department": "HR", "salary": 30000},
    {"id": 103, "name": "Charan", "department": "IT", "salary": 65000},
    {"id": 104, "name": "David", "department": "Sales", "salary": 25000},
    {"id": 105, "name": "Ezhil", "department": "HR", "salary": 55000},
    {"id": 106, "name": "Frank", "department": "Sales", "salary": 40000}
]


deptCount = {}
highestPaidEmp = ""
highestPaidNetSal = 0




def getBonus(salary):
    if (salary > 60000):
        return salary*(20/100)
    elif (salary >= 40000 and salary <=60000):
        return salary*(15/100)
    elif (salary > 30000 and salary <40000):
        return salary*(10/100)
    else:
        return salary*(5/100)



def getDeductions(salary):
    if (salary > 50000):
        return salary*(10/100)
    elif (salary >= 30000 and salary <=50000):
        return salary*(5/100)
    elif (salary < 30000):
        return salary*(2/100)
 
 



def getEmpCalculations():
    global highestPaidEmp, highestPaidNetSal
    
    for emp in employees:
    
        bonus = getBonus(emp["salary"])
        deductions=getDeductions(emp["salary"])
        netSalary = emp["salary"] + bonus - deductions
        
        print(f"{emp["id"]} {emp["name"]} {emp["department"]} {emp["salary"]}  {bonus} {deductions} {netSalary}")
        
        
        #cal. dept count
        if emp["department"] in deptCount:
            deptCount[emp["department"]] += 1
        else:
            deptCount[emp["department"]] = 1
        
        #cal. highet paid employees
        if netSalary > highestPaidNetSal:
            highestPaidNetSal=netSalary
            highestPaidEmp=emp["name"]


def displayDept():
    for department, count in deptCount.items():
        print(department, ":", count)
    
def displayHighest():
    print("Highest Paid Employee ", highestPaidEmp)
    print("Net Salary:", highestPaidNetSal)
    
    
def search_employee():
    search_id = int(input("Enter employee ID: "))

    found = False

    for employee in employees:

        if employee["id"] == search_id:

            found = True

            # Calculate bonus
            salary = employee["salary"]
            bonus = getBonus(salary)
            deduction = getDeductions(salary)
            net_salary = salary + bonus - deduction

            # Display employee details
            print("\n===== EMPLOYEE DETAILS =====")
            print("Employee ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Basic Salary:", salary)
            print("Bonus:", bonus)
            print("Deduction:", deduction)
            print("Net Salary:", net_salary)

            break

    if not found:
        print("Employee not found")





#main function
print("ID ---- Name ----- Department ------ Basic ----- Bonus ----- Deductions ----- Net Salary")
getEmpCalculations()
print("\n\nDepartment count \n")
displayDept()
print("\n\n Highest paid employee and net salary\n")
displayHighest()
print("\n\n Search employee \n")
search_employee()
    
        
    
    
    