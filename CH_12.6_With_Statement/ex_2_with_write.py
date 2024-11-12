with open('my_data.txt', 'r+') as f:
    num1 = int(f.readline())
    num2 = int(f.readline())
    product = num1 * num2
    f.write('\n' + str(product))
