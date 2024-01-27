
name = input("Enter student name: ")

subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))
subject4 = int(input("Enter marks for subject 4: "))
subject5 = int(input("Enter marks for subject 5: "))

Obtained_marks = subject1 + subject2 + subject3 +subject4 +subject5
percentage = (Obtained_marks / 500) * 100

if percentage >= 80:
    grade = 'A+'
elif percentage >= 70:
    grade = 'A'
elif percentage >= 60:
    grade = 'B'
elif percentage >= 50:
    grade = 'C'
else:
    grade = 'F'

print("\n------ Marksheet ------")
print("Name: ", name)
print("Subject 1: ", subject1)
print("Subject 2: ", subject2)
print("Subject 3: ", subject3)
print("Subject 4: ", subject4)
print("Subject 5: ", subject5)

print("Obtained_marks: ", Obtained_marks)
print("Percentage: ", percentage, "%")
print("Grade: ", grade)
