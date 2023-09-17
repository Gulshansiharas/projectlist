# l=[]
# def add():
#     name=input("enter the name:")
#     account=int(input("enter the account:"))
#     phone=int(input("enter the phone:"))
#     amount=int(input("enter the amount:"))
#     if amount>1000:
#         f = []
#         f.append(name)
#         f.append(account)
#         f.append(phone)
#         f.append(amount)
#         l.append(f)
#         print("register")
#     else:
#         print("not register")
# def deposit():
#     ac=int(input("enter the account:"))
#     p=int(input("enter the price:"))
#     for i in l:
#         if ac == i[1]:
#             i[3]+=p
#             print("deposited")
# def withdrawal():
#     ac = int(input("enter the account:"))
#     p = int(input("enter the price:"))
#     for i in l:
#         if ac == i[1]:
#             i[3]-=p
#             print("withdrayal")
# def balance():
#     ac=int(input("enter the account:"))
#     for i in l:
#         print(i[3])
# while True:
#     print("1.add account")
#     print("2.deposit")
#     print("3.withdrawal")
#     print("4.balance")
#     x=int(input("enter the choice"))
#     if x==5:
#         break
#
#     if x == 1:
#         add()
#     if x == 2:
#         deposit()
#     if x ==3:
#         withdrawal()
#     if x==4:
#         balance()
# "Deposit question"
# l=[]
# def add():
#     name=input("enter the name:")
#     account=int(input("enter the account:"))
#     phone=int(input("enter the phone:"))
#     amount=int(input("enter the amount:"))
#     f=[]
#     f.append(name)
#     f.append(account)
#     f.append(phone)
#     f.append(amount)
#     l.append(f)
#     print("account is added")
#     print(l)
# def deposit():
#     ac=int(input("enter the account:"))
#     p=int(input("enter the price:"))
#     for i in l:
#         if ac == i[1]:
#             if i[3]<100:
#                 i[3]+=p
#                 print("the amount is not deposited")
#             else:
#                 print("The amount is deposited")
#
# def withdrawal():
#     ac = int(input("enter the account:"))
#     p = int(input("enter the price:"))
#     for i in l:
#         if ac == i[1]:
#             i[3]-=p
#             print("withdrayal")
# def balance():
#     ac=int(input("enter the account:"))
#     for i in l:
#         print(i[3])
# while True:
#     print("1.add account")
#     print("2.deposit")
#     print("3.withdrawal")
#     print("4.balance")
#     x=int(input("enter the choice"))
#     if x==5:
#         break
#
#     if x == 1:
#         add()
#     if x == 2:
#         deposit()
#     if x ==3:
#         withdrawal()
#     if x==4:
#         balance()
# "withdrayal question"
l=[]
def add():
    name=input("enter the name:")
    account=int(input("enter the account:"))
    phone=int(input("enter the phone:"))
    amount=int(input("enter the amount:"))
    f = []
    f.append(name)
    f.append(account)
    f.append(phone)
    f.append(amount)
    l.append(f)
    print("The account is added")

def deposit():
    ac=int(input("enter the account:"))
    p=int(input("enter the price:"))
    for i in l:
        if ac == i[1]:
            i[3]+=p
            print("deposited")
def withdrawal():
    ac = int(input("enter the account:"))
    p = int(input("enter the price:"))
    for i in l:
        if ac == i[1]:
            i[3]-=p
            if p%100==0 or p%200==0 or p%500==0:
                    print("The note is multiple of 100 or 200 or 500")
            else:
                print("The note is not a multiple ")
            if p<1000:
                print("the account is default")
            else:
                print("the account is not default")
    print("withdrayal")
def balance():
    ac=int(input("enter the account:"))
    for i in l:
        print(i[3])
wnd(name)
        f.append(account)
        f.append(phone)
        f.append(amount)
        l.append(f)
        print("register")
    else:
        print("not register")
def deposit():
    ac=int(input("enter the account:"))
    p=int(input("enter the price:"))
    for i in l:
        if ac == i[1]:
            i[3]+=p
            print("deposited")
def withdrawal():
    ac = int(input("enter the account:"))
    p = int(input("enter the price:"))
    for i in l:
        if ac == i[1]:
            i[3]-=p
            print("withdrayal")
def balance():
    ac=int(input("enter the account:"))
    for i in l:
        print(i[3])
while True:
    print("1.add account")
    print("2.deposit")
    print("3.withdrawal")
    print("4.balance")
    x=int(input("enter the choice"))
    if x==5:
        break

    if x == 1:
        add()
    if x == 2:
        deposit()
    if x ==3:
        withdrawal()
    if x==4:
        balance()