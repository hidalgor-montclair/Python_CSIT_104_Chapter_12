import os
import sys

f = open(sys.argv[1], 'r')

num1 = int(f.readline())
num2 = int(f.readline())
f.close()

print(f"num1: {num1}")
print(f"num2: {num2}")