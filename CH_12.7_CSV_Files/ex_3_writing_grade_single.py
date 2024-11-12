import csv
with open('grades_output_1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'score'])
    writer.writerow(['Petr Little', '81.5'])
