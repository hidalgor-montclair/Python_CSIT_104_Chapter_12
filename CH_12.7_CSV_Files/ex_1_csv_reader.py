import csv
with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile)
    for row in grades_reader:
        print(row)
