---

🎓 Python Grade Calculator

This repository contains a Python program that calculates a student's **grade and performance status** based on their **marks and attendance percentage**.
It demonstrates the use of **conditional statements, logical flow, input validation, functions, and exception handling** in Python.

---

📌 Features

* Accepts marks (0–100) and attendance percentage as input
* Validates input values to prevent invalid data
* Determines grades using `if–elif–else` conditions
* Applies nested conditions for attendance-based rewards
* Handles invalid (non-numeric) input using `try–except`
* Displays meaningful grade and performance messages

---

🛠️ Technologies Used

* **Python 3**
* Built-in functions (`input()`, `print()`)
* Conditional statements and exception handling

---

📂 File Included

* **`grade_calculator.py`** – Main program that calculates grades based on marks and attendance 

---

▶️ How to Run the Program

1. Make sure **Python 3** is installed on your system.
2. Clone this repository or download the file.
3. Open a terminal in the project directory.
4. Run the script:

```bash
python grade_calculator.py
```

---

📥 Sample Output

```text
Enter marks (0-100): 92
Enter attendance percentage: 80
Grade: A+ | Status: Outstanding | Merit Certificate Eligible
```

```text
Enter marks (0-100): 45
Enter attendance percentage: 70
Grade: F | Status: Fail
```

---

📊 Grade Criteria

| Marks Range | Grade | Status      |
| ----------- | ----- | ----------- |
| ≥ 90        | A+    | Outstanding |
| 80 – 89     | A     | Excellent   |
| 70 – 79     | B     | Very Good   |
| 60 – 69     | C     | Good        |
| 50 – 59     | D     | Pass        |
| < 50        | F     | Fail        |

> **Note:** Students with **A+ grade and ≥75% attendance** are eligible for a **Merit Certificate**.

---

🎯 Learning Objectives

This project helps learners understand:

* Function creation and reuse
* Conditional logic and nested conditions
* Input validation
* Exception handling (`ValueError`)
* Real-world business rules in programming

---

👤 Author

**Tanishq Gupta**
Python Developer Intern

---
📄 License

This project is open-source and free to use for **educational and learning purposes**.

---
