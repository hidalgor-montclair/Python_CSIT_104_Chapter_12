
fruits = ['apple', 'banana', 'cherry']
f = open('myfile5.txt', 'w')
for fruit in fruits:
    f.write(fruit + '\n')
f.close()

