import csv

data = [['name', 'hw1', 'hw2'], ['Sam', 10, 10], ['Joff', 5, 6]]
with open('grades_output_2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
