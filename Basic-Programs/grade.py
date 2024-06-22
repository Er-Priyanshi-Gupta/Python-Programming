name = input("Enter your name\n")
marks = input("Enter your list marks in 5 subjects out of 100 separated by commas \n").split(",")
avgMarks = 0
for mark in marks:
    avgMarks = avgMarks + int(mark)
avgMarks = avgMarks//5
if avgMarks < 25:
    grade = 'F'
elif avgMarks >= 25 and avgMarks <= 44:
    grade = 'E'
elif avgMarks >= 45 and avgMarks <= 59:
    grade = 'D'
elif avgMarks >= 50 and avgMarks <= 69:
    grade = 'C'
elif avgMarks >= 70 and avgMarks <= 89:
    grade = 'B'
else:
    grade = 'A'
print(f"{name} grade is {grade} as your average marks are {avgMarks}")
