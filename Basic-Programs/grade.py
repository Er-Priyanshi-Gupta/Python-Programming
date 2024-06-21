name = input("Enter your name\n")
marks = input("Enter your list marks in 5 subjects out of 100\n").split(",")
avgMarks = 0
for mark in marks:
    avgMarks = avgMarks + mark
print(avgMarks)