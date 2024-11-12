import os
import sys
if not os.path.exists(sys.argv[1]):
    print("File does not exist.")
    sys.exit(1)

else:
    print(sys.argv[1] + " Was found!")
