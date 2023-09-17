from m1 import add
from m2 import sub
from m3 import prod
from m4 import div

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.division")


    x =int(input("Enter the choice:"))
    if x==5:
        break
    if x==1:
        add()
    elif x==2:
        sub()
    elif x==3:
        prod()
    else:
        div()