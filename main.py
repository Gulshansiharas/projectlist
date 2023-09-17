# i=0
# while i<10:
#     i+=1
#     if i==6:
#         pass
#     print(i)
# password=""
# while(len(password))<8:
#     print("password should atleast 8 characters")
#     password=input("enter a password:")
# print("valid password")
# while True:
#     print("1.Addition")
#     print("2.subtraction")
#     print("3,multiplication")
#     print("4.division")
#     x=int(input("enter the choice:"))
#     if x==5:
#         break
#     a=int(input("enter the first number:"))
#     b=int(input("enter the second number:"))
#     if x==1:
#         sum=a+b
#         print("The sum of 2 numbers is",sum)
#     if x==2:
#         diff=a-b
#         print("The difference of 2 numbers is",diff)
#     if x==3:
#         prod=a*b
#         print("The product of 2 numbers is",prod)
#     if x==4:
#         div=a/b
#         print("The division of 2 numbers is",div)
while True:
    print("1.Add")
    print("2.delete")
    print("3,update")
    print("4.display")
    x=int(input("enter the choice:"))
    if x==5:
        break
    l=[]
    if x==1:
        ID = int(input("enter the ID:"))
        Title = input("enter the title")
        Price = int(input("enter the price:"))
        Author= input("enter the authors:")
        Publisher= input("enter the publisher:")
        f=["ID",'Title','Price','Author',Publisher]
        l.append(f)

        print(l)
        print("The book is added")


    if x==2:
        d=int(input("enter the id:"))
        for i in l:
            if i[1]==d:
                l.remove(i)
                print(l)
        print("The book is deleted")
    if x==3:
        u=int(input("enter the Id:"))
        for i in l:
            if i[2]==u:
                l.update(i)
        print("The book is updated")

    if x==4:
        for i in l:
            print(ID,i[0])
            print(Title,i[1])
            print(Price,i[2])
            print(Author,i[3])
            print(Publisher,i[4])
        print("The book is display")