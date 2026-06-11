def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

print("===== Student Grade Tracker =====")

name = input("Enter student name: ")

subjects = int(input("Enter number of subjects: "))

marks = []

for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / subjects

grade = calculate_grade(average)

print("\n===== Result =====")
print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
print("Grade:", grade)
