l={}
while True:
    print("1.created")
    print("2.delete")
    print("3.update")
    print("4.display")
    f=int(input("enter the choice:"))
    if f==5:
        break
    if f==1:

        k=int(input("Enter the key :"))
        v=input("Enter the values:")
        h={k:v}
        l.update(h)
        print(l)
    elif f==2:
        u=int(input("Enter the key:"))
        if u in l:
            l.pop(u)
            print(l)
    elif f==3:
        v=int(input("Enter the key:"))
        if v in l:
                k=input("Enter the value:")
                print(k)
                l[v]=k
                print(l)
    elif f==4:
            print(l)


