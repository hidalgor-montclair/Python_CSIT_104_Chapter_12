f = open('D:\Github\PWA_Project\Python_CSIT_104_Chapter_12\CH_12.1_Reading_Files\my_data.txt')
lines = f.readlines()
f.close()

total = 0
for ln in lines:
    total += int(ln)

avg = total / len(lines)
print(f'Average value: {avg}')
