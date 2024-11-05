import os
print(os.getcwd())

print()
print()
print("File contents are below:")
print()
print()
my_file = open('D:\Github\PWA_Project\Python_CSIT_104_Chapter_12\CH_12.1_Reading_Files\journal.txt')

lines = my_file.readlines()  # All lines
print(lines)

my_file.close()
