# Manual Screenshots Capture Checklist

This checklist specifies the exact screens to capture from your running VS Code terminal and save into the `screenshots/` folder for your project submission or viva presentation.

---

## Instructions for Capturing in VS Code
1. Open the integrated terminal in VS Code (``Ctrl + ` ``).
2. Run the application:
   ```powershell
   py application\student_management.py
   ```
3. For each test scenario below, perform the action in the terminal.
4. Take a clean screenshot of the terminal window (using **Windows Snipping Tool**: `Windows Key + Shift + S`).
5. Save the image into the `screenshots/` folder using the suggested filename.

---

## Screenshot Checklist

| No. | Screen Scenario | Menu Option & Actions | Suggested Filename |
|:---:|---|---|---|
| **1** | **Main Menu Display** | Launch program, display the initial 13-choice menu. | `screenshots/01_main_menu.png` |
| **2** | **Display All Students** | Select `1` to display initial records for Roll 101 and 102. | `screenshots/02_display_all_students.png` |
| **3** | **Count Students** | Select `2` to show `Total students: 2`. | `screenshots/03_count_students.png` |
| **4** | **Add a New Student** | Select `3`, enter details for a new student (Roll 103, Name: Amit, Dept: Mechanical, etc.). | `screenshots/04_add_student.png` |
| **5** | **Duplicate Roll/Reg Validation** | Select `3`, enter existing Roll `101` or existing Reg `REG101` showing the validation error. | `screenshots/05_validation_duplicate.png` |
| **6** | **Search by Roll Number** | Select `4`, enter `101` to display Rahul's complete profile. | `screenshots/06_search_student.png` |
| **7** | **Update Student Details** | Select `5`, enter `101`, choose option `7` to update marks for `Python`. | `screenshots/07_update_student.png` |
| **8** | **Calculate Individual Average** | Select `7`, enter `101` to show total marks and computed average. | `screenshots/08_student_average.png` |
| **9** | **Display Highest Scorer** | Select `8` to show highest scoring student (Priya, Roll 102). | `screenshots/09_highest_scorer.png` |
| **10** | **Search by Department** | Select `9`, enter `computer` showing case-insensitive match. | `screenshots/10_department_search.png` |
| **11** | **Overall Institutional Average** | Select `10` showing total marks and overall average across all students. | `screenshots/11_overall_average.png` |
| **12** | **Department-wise Counts** | Select `11` showing department frequency count dictionary. | `screenshots/12_department_counts.png` |
| **13** | **Display Collections Used** | Select `12` showing sets of departments, subjects, and clubs. | `screenshots/13_collections_display.png` |
| **14** | **Clean Exit** | Select `13` showing `"Program closed."` message. | `screenshots/14_exit_screen.png` |
