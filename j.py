from jam import add,sub,prod,div
while True:
    print("1.add")
    print("2.sub")
    print("3.prod")
    print("4.div")
    x=int(input("enter the choice:"))
    if x==5:
        break
    if x==1:
        add.sum()
    if x==2:
        sub.diff()
    if x==3:
        prod.multiplication()
    if x==4:
        div.division()