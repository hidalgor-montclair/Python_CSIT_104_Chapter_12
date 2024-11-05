"""Echo the contents of a file."""
f = open('D:\Github\PWA_Project\Python_CSIT_104_Chapter_12\CH_12.1_Reading_Files\journal.txt')

for line in f:
    print(line, end="")

f.close()