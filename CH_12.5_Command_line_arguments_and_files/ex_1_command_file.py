import sys
if len(sys.argv) != 2:
    print("Oh no, you typed the argument wrong!")
    print("Usage: python ex_1_command_file.py <filename>")
    # print(sys.argv)
    sys.exit(1)

print("The right file was put into the argument")
