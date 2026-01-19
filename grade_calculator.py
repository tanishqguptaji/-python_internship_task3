
def calculate_grade(marks, attendance):
    """
    Determines grade based on marks and attendance
    """

    # Validate marks
    if marks < 0 or marks > 100:
        return "Invalid marks! Please enter marks between 0 and 100."

    # Validate attendance
    if attendance < 0 or attendance > 100:
        return "Invalid attendance! Enter attendance between 0 and 100."

    # Grade determination
    if marks >= 90:
        grade = "A+"
        if attendance >= 75:
            return f"Grade: {grade} | Status: Outstanding | Merit Certificate Eligible"
        else:
            return f"Grade: {grade} | Status: Outstanding"

    elif marks >= 80:
        grade = "A"
        return f"Grade: {grade} | Status: Excellent"

    elif marks >= 70:
        grade = "B"
        return f"Grade: {grade} | Status: Very Good"

    elif marks >= 60:
        grade = "C"
        return f"Grade: {grade} | Status: Good"

    elif marks >= 50:
        grade = "D"
        return f"Grade: {grade} | Status: Pass"

    else:
        grade = "F"
        return f"Grade: {grade} | Status: Fail"


# -------- MAIN PROGRAM --------

try:
    marks = float(input("Enter marks (0-100): "))
    attendance = float(input("Enter attendance percentage: "))

    result = calculate_grade(marks, attendance)
    print(result)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
