# Create a grading system with nested if-else(A+,A,B+,B,C,Fail).
marks = int(input("Enter your marks: "))

if marks >=90:
    grade = 'A+'
elif marks >= 80:
    grade = 'A'
elif marks >= 70:
    grade = 'B+'
elif marks >= 60:
    grade = 'B'
elif marks >= 40:
    grade = 'c'
else:
    grade = 'Fail'

print("You got grade: ",grade)
