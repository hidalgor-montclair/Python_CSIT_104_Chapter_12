import os

print("Checking for existing file")
if os.path.exists('journal.txt'):
    print("File found!")
else:
    print("File not found!")


print("Checking for non-existing file")
if os.path.exists('nonexistant.txt'):
    print("File found!")
else:
    print("File not found!")