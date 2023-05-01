length1 = int(input("What is the length for your first rectangle?: "))
width1 = int(input("What is the width for your first rectangle?: "))

length2 = int(input("What is the length for your second  rectangle?: "))
width2 = int(input("What is the width for your second rectangle?: "))

area1 = length1 * width1
area2 = length2 * width2

if area1 > area2:
    print('Rectangle 1 has the greater value.')
else:
    if area1 < area2:
        print('Rectangle 2 has the greater value.')
    else:
        print('Both have the same area')
