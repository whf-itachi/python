import re

found = False
x = [1, 2, 3, 4, 5, 6, 76]
while x:
    print(x)
    if re.match('3', str(x[0])):
        print("Ni")
        break
    x = x[1:]
else:
    print("not found")
