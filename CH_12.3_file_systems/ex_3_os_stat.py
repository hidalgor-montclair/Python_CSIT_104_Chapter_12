import os
file_info = os.stat('myfile.txt')

size = os.path.getsize('myfile.txt')

print()
print("file info below:")
print()
print(file_info)
print()
print("file size below:")
print(f"File size: {size} bytes")
print()
