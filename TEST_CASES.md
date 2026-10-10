# Comprehensive Test Suite & Execution Log

**Project**: Student Record and Academic Management System  
**Target File**: `application/student_management.py` (Read-Only)  
**Python Version**: Python 3.14.7  
**Execution Environment**: Windows PowerShell CLI  

---

## 1. Test Summary Matrix

| Category | Total Tests | Passed | Failed |
|---|:---:|:---:|:---:|
| Menu & Navigation | 3 | 3 | 0 |
| Read / Query Operations | 6 | 6 | 0 |
| Create / Validation Operations | 7 | 7 | 0 |
| Update Operations | 4 | 4 | 0 |
| Delete Operations | 3 | 3 | 0 |
| Statistical Computations | 4 | 4 | 0 |
| **Total** | **27** | **27** | **0** |

---

## 2. Detailed Test Cases & Verifications

### 2.1 Menu & Navigation Tests

#### TC-01: Main Menu Display & Exit
- **Objective**: Verify that the application initializes, displays all 13 menu choices, and exits cleanly when option 13 is selected.
- **Input**: `13`
- **Expected Result**: Program displays menu, outputs `"Program closed."`, and terminates with exit code 0.
- **Actual Result**:
  ```text
  ========== STUDENT MANAGEMENT SYSTEM ==========
  1. Display Students
  ...
  13. Exit
  Enter your choice: Program closed.
  ```
- **Status**: **PASS**

#### TC-02: Invalid Menu Choice (Out of Bounds)
- **Objective**: Verify that choosing a non-existent option does not crash the program and returns to the menu.
- **Input**: `99` followed by `13`
- **Expected Result**: Displays `"Invalid choice!"` and returns to menu loop.
- **Actual Result**: Output showed `"Invalid choice!"` and re-prompted menu.
- **Status**: **PASS**

#### TC-03: Invalid Menu Choice (Non-numeric String)
- **Objective**: Verify that entering alphabetic characters as menu choice is handled gracefully.
- **Input**: `abc` followed by `13`
- **Expected Result**: Displays `"Invalid choice!"` and returns to menu loop.
- **Actual Result**: Output showed `"Invalid choice!"` and re-prompted menu.
- **Status**: **PASS**

---

### 2.2 Read and Query Operations

#### TC-04: Display All Students (Initial State)
- **Objective**: Verify that pre-populated students (Roll 101 and Roll 102) are rendered with all fields.
- **Input**: `1` followed by `13`
- **Expected Result**: Formatted student cards for Rahul (101) and Priya (102).
- **Actual Result**: Full student cards printed with Roll No, Reg No, Name, Department, Semester, Subjects, Marks, Attendance, Email, Phone, Address, and Clubs.
- **Status**: **PASS**

#### TC-05: Count Students
- **Objective**: Verify that student count matches total items in `students` list.
- **Input**: `2` followed by `13`
- **Expected Result**: `Total students: 2`
- **Actual Result**: `Total students: 2`
- **Status**: **PASS**

#### TC-06: Search Existing Student by Roll Number
- **Objective**: Verify accurate retrieval of student profile by Roll No.
- **Input**: `4`, then `101`, then `13`
- **Expected Result**: Displays details for Rahul (Roll No 101).
- **Actual Result**: Displayed all profile information for Roll 101.
- **Status**: **PASS**

#### TC-07: Search Missing Student by Roll Number
- **Objective**: Verify response when requested roll number does not exist.
- **Input**: `4`, then `999`, then `13`
- **Expected Result**: Output `"Student not found!"`.
- **Actual Result**: Output printed `"Student not found!"`.
- **Status**: **PASS**

#### TC-08: Search Student with Invalid Input Type
- **Objective**: Verify handling of non-integer roll number.
- **Input**: `4`, then `abc`, then `13`
- **Expected Result**: Output `"Roll number must be a number!"`.
- **Actual Result**: Exception caught by `try-except ValueError`, output printed `"Roll number must be a number!"`.
- **Status**: **PASS**

#### TC-09: Search by Department (Case-Insensitive)
- **Objective**: Verify that department query matches regardless of letter casing.
- **Input**: `9`, then `"computer"`, then `13`
- **Expected Result**: Displays Priya (Department: "Computer").
- **Actual Result**: Output matched Priya using `.casefold()` comparison.
- **Status**: **PASS**

#### TC-10: Search by Department with No Matches
- **Objective**: Verify message when no student belongs to queried department.
- **Input**: `9`, then `"Civil"`, then `13`
- **Expected Result**: Output `"No students found in this department!"`.
- **Actual Result**: Output printed `"No students found in this department!"`.
- **Status**: **PASS**

---

### 2.3 Create & Input Validation Operations

#### TC-11: Add Valid Student with Boundary Marks
- **Objective**: Verify successful student addition including boundary marks ($0$ and $100$).
- **Input**:
  - Roll No: `103`
  - Reg No: `REG103`
  - Name: `Amit`
  - Dept: `Mechanical`
  - Semester: `2`
  - Email: `amit@example.com`
  - Phone: `9876543212`
  - Address: `Pune`
  - Number of subjects: `2`
  - Subject 1: `Python`, Marks: `100`, Attendance: `95`
  - Subject 2: `CAD`, Marks: `0`, Attendance: `90`
- **Expected Result**: `"Student added successfully!"`, total students becomes `3`.
- **Actual Result**: Output confirmed addition; subsequent `Count Students` output `Total students: 3`.
- **Status**: **PASS**

#### TC-12: Duplicate Roll Number Validation
- **Objective**: Prevent registering a student with an already existing roll number.
- **Input**: `3`, then `101`
- **Expected Result**: `"Roll number already exists!"` and returns to menu.
- **Actual Result**: `"Roll number already exists!"`
- **Status**: **PASS**

#### TC-13: Duplicate Registration Number Validation
- **Objective**: Prevent registering a student with an already existing registration code.
- **Input**: `3`, Roll `105`, Reg No `"REG101"`
- **Expected Result**: `"Registration number already exists!"` and returns to menu.
- **Actual Result**: `"Registration number already exists!"`
- **Status**: **PASS**

#### TC-14: Semester Out-of-Bounds Validation
- **Objective**: Enforce $1 \le \text{Semester} \le 8$.
- **Input**: `3`, Roll `105`, Reg No `REG105`, Name `Neha`, Dept `Computer`, Semester `9`
- **Expected Result**: `"Semester must be between 1 and 8!"`
- **Actual Result**: `"Semester must be between 1 and 8!"`
- **Status**: **PASS**

#### TC-15: Marks Above Range Validation
- **Objective**: Prevent marks greater than 100.
- **Input**: `3`, Roll `105`, Reg `REG105`, Name `Neha`, Dept `Computer`, Sem `1`, Email `e@e.com`, Phone `123`, Addr `City`, Sub count `1`, Subject `Math`, Mark `105`
- **Expected Result**: `"Marks must be between 0 and 100!"`
- **Actual Result**: `"Marks must be between 0 and 100!"`
- **Status**: **PASS**

#### TC-16: Attendance Below Range Validation
- **Objective**: Prevent attendance percentage below 0.
- **Input**: `3`, Roll `105`, Reg `REG105`, Name `Neha`, Dept `Computer`, Sem `1`, Email `e@e.com`, Phone `123`, Addr `City`, Sub count `1`, Subject `Math`, Mark `80`, Attendance `-5`
- **Expected Result**: `"Attendance must be between 0 and 100!"`
- **Actual Result**: `"Attendance must be between 0 and 100!"`
- **Status**: **PASS**

---

### 2.4 Update Operations

#### TC-17: Update Non-Existent Student
- **Objective**: Verify handling when attempting to update an unknown roll number.
- **Input**: `5`, then `999`
- **Expected Result**: `"Student not found!"`
- **Actual Result**: `"Student not found!"`
- **Status**: **PASS**

#### TC-18: Update Student Name
- **Objective**: Verify modifying the name of an existing student.
- **Input**: `5`, Roll `101`, Sub-choice `1`, New Name `"Rahul S"`
- **Expected Result**: `"Student details updated successfully!"`
- **Actual Result**: Output confirmed successful update.
- **Status**: **PASS**

#### TC-19: Update Marks for Existing Subject
- **Objective**: Verify modifying the mark of a specific subject entry.
- **Input**: `5`, Roll `101`, Sub-choice `7`, Subject `"Python"`, New Marks `99`
- **Expected Result**: `"Student details updated successfully!"`
- **Actual Result**: Output confirmed update; subject mark at index 0 updated to 99.
- **Status**: **PASS**

#### TC-20: Update Marks for Non-Existent Subject
- **Objective**: Verify response when updating a subject not in student's subject list.
- **Input**: `5`, Roll `101`, Sub-choice `7`, Subject `"Biology"`
- **Expected Result**: `"Subject not found!"`
- **Actual Result**: `"Subject not found!"`
- **Status**: **PASS**

---

### 2.5 Delete Operations

#### TC-21: Delete Non-Existent Student
- **Objective**: Verify handling when deleting an invalid roll number.
- **Input**: `6`, then `999`
- **Expected Result**: `"Student not found!"`
- **Actual Result**: `"Student not found!"`
- **Status**: **PASS**

#### TC-22: Delete Existing Student
- **Objective**: Verify deletion of student record and subsequent count update.
- **Input**: `6`, then `101`
- **Expected Result**: `"Student deleted successfully!"`, count drops from 2 to 1.
- **Actual Result**: Record removed; subsequent count operation returned `Total students: 1`.
- **Status**: **PASS**

#### TC-23: Delete All Students and Verify Empty List State
- **Objective**: Verify program behavior when deleting all records until list is empty.
- **Input**: Delete `101`, then delete `102`
- **Expected Result**: Total count becomes `0`.
- **Actual Result**: `Total students: 0`. Program did not crash.
- **Status**: **PASS**

---

### 2.6 Statistical Computations & Collections

#### TC-24: Individual Student Average Marks Calculation
- **Objective**: Compute average for student with marks $[85, 90, 78]$.
- **Input**: `7`, Roll `101`
- **Calculation**: $\text{Total} = 253$, $\text{Average} = \frac{253}{3} \approx 84.333\dots$
- **Expected Result**: Total: 253, Average: 84.33
- **Actual Result**: `Total marks: 253`, `Average marks: 84.33`
- **Status**: **PASS**

#### TC-25: Highest Scorer Identification
- **Objective**: Identify student with highest average among initial records.
- **Input**: `8`
- **Calculation**: Rahul avg = $84.33$, Priya avg = $\frac{92+88+95}{3} = 91.67$.
- **Expected Result**: Priya (Roll No 102) with 91.67.
- **Actual Result**: `Student name: Priya`, `Roll number: 102`, `Average marks: 91.67`
- **Status**: **PASS**

#### TC-26: Institutional Overall Average Calculation
- **Objective**: Compute average across all subject entries across all students.
- **Input**: `10`
- **Calculation**: Total marks = $253 + 275 = 528$, Total entries = $6$, Average = $\frac{528}{6} = 88.0$.
- **Expected Result**: Total marks: 528, Entries: 6, Overall average: 88.0
- **Actual Result**: `Total marks: 528`, `Total subject entries: 6`, `Overall average: 88.0`
- **Status**: **PASS**

#### TC-27: Department-wise Frequency Counts
- **Objective**: Count occurrences of students per department.
- **Input**: `11`
- **Expected Result**: `AI & ML : 1`, `Computer : 1`
- **Actual Result**: `AI & ML : 1`, `Computer : 1`
- **Status**: **PASS**
