import csv

with open('grades.csv', 'r') as csvfile:
    grades_reader = csv.reader(csvfile)
    for row in grades_reader:
        # Skip the header row
        if row[0] == 'name':
            continue
        # Calculate score
        name = row[0]
        final_score = sum([float(x) for x in row[1:]])
        print(f"{name}'s final score is {final_score}")
