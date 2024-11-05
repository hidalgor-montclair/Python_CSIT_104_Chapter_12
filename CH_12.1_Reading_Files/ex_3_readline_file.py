import os
print(os.getcwd())

print()
print()
print("File contents are below:")
print()
print()
my_file = open('D:\Github\PWA_Project\Python_CSIT_104_Chapter_12\CH_12.1_Reading_Files\journal.txt')

line = my_file.readline()
print(line)

my_file.close()
