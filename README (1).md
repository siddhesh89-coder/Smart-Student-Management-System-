# Student Record and Academic Management System
**Data Organization and Management Using Python Collections**

---

## 1. Project Overview

The **Student Record and Academic Management System** is a menu-driven Python application designed for first-year engineering and computer science students. The system demonstrates the practical application of Python built-in collection data types—**Strings, Lists, Tuples, Sets, and Dictionaries**—for storing, organizing, and manipulating student academic data in memory.

---

## 2. Project Folder Structure

```text
Student_Record_Academic_Management_System/
│
├── application/
│   └── student_management.py    # Main menu-driven Python application (Read-Only)
│
├── documentation/
│   ├── PROJECT_REPORT.md        # Comprehensive academic project report
│   ├── TEST_CASES.md            # Verified test suite with inputs and actual results
│   └── SCREENSHOTS_CHECKLIST.md # Checklist of exact screens to capture manually
│
├── programs/                    # Practice programs folder
│
├── screenshots/                 # Destination folder for manual terminal screenshots
│
└── README.md                    # Project guidance and execution instructions
```

---

## 3. How to Run the Program in VS Code

### Prerequisites
- Python 3.x installed (verified with Python 3.14 on Windows using the `py` launcher).

### Execution Steps
1. **Open Workspace**: Open the `Student_Record_Academic_Management_System` folder in Visual Studio Code.
2. **Open Integrated Terminal**:
   - Press ``Ctrl + ` `` (Backtick) or navigate to **Terminal -> New Terminal** from the top menu.
3. **Verify Directory**:
   Ensure your terminal prompt is at the project root directory:
   ```powershell
   c:\Users\sarth\Downloads\Student_Record_Academic_Management_System
   ```
4. **Run the Program**:
   Execute the following command in PowerShell / Command Prompt:
   ```powershell
   py application\student_management.py
   ```
   *(Alternatively, if `python` is configured in your system PATH, you can use: `python application/student_management.py`)*

5. **Interact with the Menu**:
   Enter numbers `1` through `13` to navigate features. Type `13` to exit cleanly.

---

## 4. Main Menu Operations

The application provides 13 core operations:

| Choice | Operation | Description |
|---|---|---|
| **1** | Display Students | Lists all registered student records with complete details. |
| **2** | Count Students | Displays total number of students currently registered. |
| **3** | Add Student | Registers a new student with roll number, registration number, semester, subjects, marks, and attendance. |
| **4** | Search Student | Searches and retrieves student profile using Roll Number. |
| **5** | Update Student | Modifies student details (Name, Department, Semester, Email, Phone, Address, Marks, Attendance). |
| **6** | Delete Student | Removes a student record by Roll Number. |
| **7** | Calculate Average Marks | Computes total and average percentage for an individual student. |
| **8** | Show Highest Scorer | Identifies the student with the highest average marks across their subjects. |
| **9** | Search by Department | Performs case-insensitive search and lists all students in a department. |
| **10** | Overall Average | Computes aggregate academic average across all student records. |
| **11** | Department-wise Count | Generates student frequency counts grouped by department. |
| **12** | Show Collections | Displays current unique departments, unique subjects, and student clubs. |
| **13** | Exit | Terminates the program cleanly. |

---

## 5. Python Collections Demonstrated

| Collection Type | Application in Project | Example in Code |
|---|---|---|
| **Strings (`str`)** | Student names, registration numbers, departments, contact numbers, email addresses, and home addresses. | `"name": "Rahul"`, `"REG101"`, `"Shirdi"` |
| **Lists (`list`)** | Primary student repository (`students`), subject list (`subjects`), academic marks (`marks`), and attendance percentages (`attendance`). | `["Python", "Mathematics", "Physics"]`, `[85, 90, 78]` |
| **Tuples (`tuple`)** | Immutable records such as Date of Birth `(Day, Month, Year)` stored in initial demonstration records. | `"dob": (15, 8, 2007)` |
| **Sets (`set`)** | Storing distinct, unordered items without duplicates: department names, subject registry, and student clubs. | `departments = {"AI & ML", "Computer", ...}`, `{"Coding Club", "AI Club"}` |
| **Dictionaries (`dict`)** | Structured key-value storage for individual student records and dynamic department frequency counts. | `{"roll_no": 101, ...}`, `department_count = {"Computer": 1, ...}` |

---

## 6. Syllabus Compliance & Design Constraints

This project strictly adheres to a beginner, first-year Python syllabus:
- **No external third-party libraries** (uses only standard Python).
- **No classes, inheritance, or OOP complexity** (purely procedural and function-based).
- **No persistent files or databases** (all data structures operate in-memory).
- **No JSON, APIs, or decorators**.
- Built with simple functions, `for`/`while` loops, conditional `if-elif-else` branching, string methods (`strip()`, `casefold()`), list methods, and basic `try-except ValueError` blocks for numeric inputs.
