
student1={
    "roll_no":101,
    "registration_no":"REG101",
    "name":"Rahul",
    "department":"AI & ML",
    "semester":1,
    "dob":(15,8,2007),
    "subjects":["Python","Mathematics","Physics"],
    "marks":[85,90,78],
    "attendance":[90,85,95],
    "clubs":{"Coding Club","AI Club"},
    "email":"rahul@example.com",
    "phone":"9876543210",
    "address":"Shirdi"
}

student2={
    "roll_no":102,
    "registration_no":"REG102",
    "name":"Priya",
    "department":"Computer",
    "semester":1,
    "dob":(10,5,2007),
    "subjects":["Python","Mathematics","Physics"],
    "marks":[92,88,95],
    "attendance":[96,90,98],
    "clubs":{"Robotics Club"},
    "email":"priya@example.com",
    "phone":"9876543211",
    "address":"Nashik"
}

students=[student1,student2]

departments={"AI & ML","Computer","Mechanical","Electronics"}
all_subjects={"Python","Mathematics","Physics","Cyber Security"}


def find_student(roll_no):
    for s in students:
        if s["roll_no"]==roll_no:
            return s
    return None


def count_students():
    print("Total students:",len(students))


def display_students():
    if not students:
        print("No student records available!")
        return

    print("\n========== ALL STUDENTS ==========")

    for s in students:
        print("\nRoll Number:",s["roll_no"])
        print("Registration Number:",s["registration_no"])
        print("Name:",s["name"])
        print("Department:",s["department"])
        print("Semester:",s["semester"])
        print("Subjects:",s["subjects"])
        print("Marks:",s["marks"])
        print("Attendance:",s["attendance"])
        print("Email:",s["email"])
        print("Phone:",s["phone"])
        print("Address:",s["address"])
        print("Clubs:",s["clubs"])
        print("-----------------------------")


def add_student():
    print("\n========== ADD STUDENT ==========")

    try:
        roll_no=int(input("Enter roll number:"))

        if find_student(roll_no) is not None:
            print("Roll number already exists!")
            return

        registration_no=input("Enter registration number:")

        if not registration_no.strip():
            print("Registration number cannot be empty!")
            return

        for s in students:
            if s["registration_no"].casefold()==registration_no.casefold():
                print("Registration number already exists!")
                return

        name=input("Enter student name:")
        department=input("Enter department:")
        semester=int(input("Enter semester:"))

        if not name.strip() or not department.strip():
            print("Name and department cannot be empty!")
            return

        if not 1<=semester<=8:
            print("Semester must be between 1 and 8!")
            return

        email=input("Enter email:")
        phone=input("Enter phone number:")
        address=input("Enter address:")

        subjects=[]
        marks=[]
        attendance=[]

        number_of_subjects=int(input("Enter number of subjects:"))

        if not 1<=number_of_subjects<=10:
            print("Number of subjects must be between 1 and 10!")
            return

        for i in range(number_of_subjects):
            subject=input("Enter subject name:")
            if not subject.strip():
                print("Subject name cannot be empty!")
                return

            mark=float(input("Enter marks (0-100):"))
            if not 0<=mark<=100:
                print("Marks must be between 0 and 100!")
                return

            attend=float(input("Enter attendance percentage (0-100):"))
            if not 0<=attend<=100:
                print("Attendance must be between 0 and 100!")
                return

            subjects.append(subject)
            marks.append(mark)
            attendance.append(attend)

        student={
            "roll_no":roll_no,
            "registration_no":registration_no,
            "name":name,
            "department":department,
            "semester":semester,
            "dob":(),
            "subjects":subjects,
            "marks":marks,
            "attendance":attendance,
            "clubs":set(),
            "email":email,
            "phone":phone,
            "address":address
        }

        students.append(student)
        departments.add(department)

        for subject in subjects:
            all_subjects.add(subject)

        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter the correct data type.")


def search_student():
    print("\n========== SEARCH STUDENT ==========")

    try:
        roll_no=int(input("Enter roll number:"))
        s=find_student(roll_no)

        if s is None:
            print("Student not found!")
            return

        print("Name:",s["name"])
        print("Roll Number:",s["roll_no"])
        print("Registration Number:",s["registration_no"])
        print("Department:",s["department"])
        print("Semester:",s["semester"])
        print("Subjects:",s["subjects"])
        print("Marks:",s["marks"])
        print("Attendance:",s["attendance"])
        print("Email:",s["email"])
        print("Phone:",s["phone"])
        print("Address:",s["address"])
        print("Clubs:",s["clubs"])

    except ValueError:
        print("Roll number must be a number!")


def update_student():
    print("\n========== UPDATE STUDENT ==========")

    try:
        roll_no=int(input("Enter roll number to update:"))
        s=find_student(roll_no)

        if s is None:
            print("Student not found!")
            return

        print("1. Update name")
        print("2. Update department")
        print("3. Update semester")
        print("4. Update email")
        print("5. Update phone")
        print("6. Update address")
        print("7. Update marks")
        print("8. Update attendance")

        choice=input("Enter your choice:")

        if choice=="1":
            name=input("Enter new name:")
            if name.strip():
                s["name"]=name
            else:
                print("Name cannot be empty!")
                return

        elif choice=="2":
            department=input("Enter new department:")
            if department.strip():
                s["department"]=department
                departments.add(department)
            else:
                print("Department cannot be empty!")
                return

        elif choice=="3":
            semester=int(input("Enter new semester:"))
            if 1<=semester<=8:
                s["semester"]=semester
            else:
                print("Semester must be between 1 and 8!")
                return

        elif choice=="4":
            s["email"]=input("Enter new email:")

        elif choice=="5":
            s["phone"]=input("Enter new phone:")

        elif choice=="6":
            s["address"]=input("Enter new address:")

        elif choice=="7":
            subject=input("Enter subject name:")
            if subject not in s["subjects"]:
                print("Subject not found!")
                return

            index=s["subjects"].index(subject)
            marks=float(input("Enter new marks (0-100):"))

            if 0<=marks<=100:
                s["marks"][index]=marks
            else:
                print("Marks must be between 0 and 100!")
                return

        elif choice=="8":
            subject=input("Enter subject name:")
            if subject not in s["subjects"]:
                print("Subject not found!")
                return

            index=s["subjects"].index(subject)
            attendance=float(input("Enter new attendance (0-100):"))

            if 0<=attendance<=100:
                s["attendance"][index]=attendance
            else:
                print("Attendance must be between 0 and 100!")
                return

        else:
            print("Invalid choice!")
            return

        print("Student details updated successfully!")

    except ValueError:
        print("Invalid input!")


def delete_student():
    print("\n========== DELETE STUDENT ==========")

    try:
        roll_no=int(input("Enter roll number to delete:"))
        s=find_student(roll_no)

        if s is None:
            print("Student not found!")
            return

        students.remove(s)
        print("Student deleted successfully!")

    except ValueError:
        print("Roll number must be a number!")


def calculate_average():
    print("\n========== AVERAGE MARKS ==========")

    try:
        roll_no=int(input("Enter roll number:"))
        s=find_student(roll_no)

        if s is None:
            print("Student not found!")
            return

        if not s["marks"]:
            print("No marks available!")
            return

        total=sum(s["marks"])
        average=total/len(s["marks"])

        print("Student name:",s["name"])
        print("Total marks:",total)
        print("Average marks:",round(average,2))

    except ValueError:
        print("Roll number must be a number!")


def highest_scorer():
    print("\n========== HIGHEST SCORER ==========")

    scored_students=[]

    for s in students:
        if s["marks"]:
            average=sum(s["marks"])/len(s["marks"])
            scored_students.append((average,s))

    if not scored_students:
        print("No marks available!")
        return

    highest_average,highest=max(scored_students,key=lambda item:item[0])

    print("Student name:",highest["name"])
    print("Roll number:",highest["roll_no"])
    print("Average marks:",round(highest_average,2))


def search_by_department():
    print("\n========== SEARCH BY DEPARTMENT ==========")
    department=input("Enter department name:")
    found=False

    for s in students:
        if s["department"].casefold()==department.casefold():
            print("Name:",s["name"])
            print("Roll Number:",s["roll_no"])
            print("Department:",s["department"])
            print("Semester:",s["semester"])
            print("--------------------")
            found=True

    if not found:
        print("No students found in this department!")


def overall_average():
    print("\n========== OVERALL AVERAGE ==========")

    total_marks=0
    total_subjects=0

    for s in students:
        total_marks+=sum(s["marks"])
        total_subjects+=len(s["marks"])

    if total_subjects==0:
        print("No marks available!")
        return

    print("Total marks:",total_marks)
    print("Total subject entries:",total_subjects)
    print("Overall average:",round(total_marks/total_subjects,2))


def department_counts():
    print("\n========== DEPARTMENT-WISE COUNT ==========")

    department_count={}

    for s in students:
        department=s["department"]

        if department in department_count:
            department_count[department]+=1
        else:
            department_count[department]=1

    if not department_count:
        print("No student records available!")
        return

    for department,count in department_count.items():
        print(department,":",count)


def show_collections():
    print("\n========== COLLECTIONS ==========")
    print("Departments:",departments)
    print("All subjects:",all_subjects)

    clubs=set()

    for s in students:
        clubs.update(s["clubs"])

    print("Student clubs:",clubs)


while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Display Students")
    print("2. Count Students")
    print("3. Add Student")
    print("4. Search Student")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Calculate Average Marks")
    print("8. Show Highest Scorer")
    print("9. Search by Department")
    print("10. Overall Average")
    print("11. Department-wise Count")
    print("12. Show Collections")
    print("13. Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        display_students()
    elif choice=="2":
        count_students()
    elif choice=="3":
        add_student()
    elif choice=="4":
        search_student()
    elif choice=="5":
        update_student()
    elif choice=="6":
        delete_student()
    elif choice=="7":
        calculate_average()
    elif choice=="8":
        highest_scorer()
    elif choice=="9":
        search_by_department()
    elif choice=="10":
        overall_average()
    elif choice=="11":
        department_counts()
    elif choice=="12":
        show_collections()
    elif choice=="13":
        print("Program closed.")
        break
    else:
        print("Invalid choice!")




















