# 13.Take total marks of 5 subjects and calculate percentage.

maths = float(input("Enter marks obtained in maths: "))
physics = float(input("Enter marks obtained in physics: "))
chemistry = float(input("Enter marks obtained in chemistry: "))
Biology = float(input("Enter marks obtained in Biology: "))
English = float(input("Enter marks obtained in English: "))

totalMarks = maths+physics+chemistry+Biology+English

percentage = (totalMarks/500)*100

print(f"Total Marks you got in Exam: {totalMarks}")
print(f"Pecentage of {totalMarks} you got {percentage}%")
