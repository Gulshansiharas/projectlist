# while True:
#     print("1..Addition")
#     print("2.Subtraction")
#     print("3.Multiplication")
#     print("4.Division")
#     x=int(input("Enter ur choice:"))
#     if x==5:
#         break
#     num1=int(input("Enter first number:"))
#     num2=int(input("Enter second number:"))
#     if x==1:
#         print("The sum is ", num1+num2)
#     if x==2:
#         print("The difference is ", num1-num2)
#     if x==3:
#         print("The product is ",num1*num2)
#     if x==4:
#         print("The division is ",num1/num2)
# Perimeter of a circle
# while True:
#     print("1.Circle")
#     print("2.Rectangle")
#     print("3.square")
#     n= int(input("Enter your choice:"))
#     if n ==4:
#         break
#     if n ==1:
#        r=int(input("Enter the radius:"))
#        print("The perimeter of a circle is ",2*3.14*r)
#     if n==2:
#         h=int(input("Enter the height:"))
#         w=int(input("Enter the width:"))
#         print("The perimeter of a rectangle is ",2*(h+w))
#     if n==3:
#         s=int(input("Enter the side:"))
#         print("The perimeter of a square is ",4*s)
# main=[[1,'ab',23,'jk rowling','hk']]
# while True:
#     print("1.Add book")
#     print("2.Delete book")
#     print("3.update book")
#     print("4.Display book")
#     f=int(input("Enter ur choice:"))
#     if f==5:
#         break
#     if f==1:
#         ID=input("Enter ID")
#         title=input("enter the title of book:")
#         price=input("price of book:")
#         author=input("Authors name:")
#         pub=input("publishers name:")
#         f=[]
#         f.append(ID)
#         f.append(title)
#         f.append(price)
#         f.append(author)
#         f.append(pub)
#         main.append(f)
#         print("The book added")
#     if f==2:
#         d=int(input("enter the ID"))
#         for i in main:
#             if i[0]==d:
#                 main.remove(i)
#         print("The book deleted")
#     if f==3:
#         c=int(input("enter id"))
#         for i in main:
#             if i[0]==c:
#                 p=int(input("enter the price"))
#                 i[2]=p
#                 print("price updated")
#
#     if f==4:
#         for i in main:
#             print("ID",i[0])
#             print("title",i[1])
#             print("price",i[2])
#             print("authors",i[3])
#             print("pub",i[4])
# list=[]
# while True:
#     print("1.add vehicle")
#     print("2.display vehicle")
#     x=int(input("enter the choice:"))
#
#     if x==3:
#         break
#     if x==1:
#       no=int(input("enter no of vehicle:"))
#       name=input("enter name:")
#       price=int(input("enter price:"))
#       wheel=int(input("enter no of tyre:"))
#       j=[]
#       j.append(no)
#       j.append(name)
#       j.append(price)
#       j.append(wheel)
#       list.append(j)
#       print(list)
#       print("The list is added")
#     if x==2:
#         while True:
#             print("1.2 wheeler")
#             print("2.3 wheeler")
#             print("3.4 wheeler")
#             r=int(input("enter ur choice:"))
#             if r == 4:
#                 break
#             if r == 1:
#                 for i in list:
#                     print(i)
#                     if i[3] == 2:
#                         print("no",i[0])
#                         print("name",i[1])
#                         print("price",i[2])
#                         print("wheel",i[3])
#             if r==2:
#                 for i in list:
#                     if i[3]==3:
#                         print("no", i[0])
#                         print("name", i[1])
#                         print("price", i[2])
#                         print("wheel", i[3])
#             if r==3:
#                 for i in list:
#                     if i[3]==4:
#                         print("no", i[0])
#                         print("name", i[1])
#                         print("price", i[2])
#                         print("wheel", i[3]
# main=[[1,'ab',23,'jk rowling','hk']]
# while True:
#      print("1.Add book")
#      print("2.Delete book")
#      print("3.update book")
#      print("4.Display book")
#      f=int(input("Enter ur choice:"))
#      if f==5:
#          break
#      if f==1:
#          ID=input("Enter ID")
#          title=input("enter the title of book:")
#          price=input("price of book:")
#          author=input("Authors name:")
#          pub=input("publishers name:")
#          f=[]
#          f.append(ID)
#          f.append(title)
#          f.append(price)
#          f.append(author)
#          f.append(pub)
#          main.append(f)
#          print("The book added")
#      if f==2:
#          d=int(input("enter the ID"))
#          for i in main:
#              if i[0]==d:
#                  main.remove(i)
#                  print("The book deleted")
#      if f==3:
#         n=input("enter the id")
#         while True:
#             print("1.title")
#             print("2.author")
#             print("3.price")
#             print("4.publishers")
#
#             c=input("enter choice")
#             if c==1:
#                 for i in main:
#                     if i[0]==n:
#                         p=input("enter the title")
#                         i[1]=p
#                         print("title updated")
#             if c==2:
#                 for i in main:
#                     if i[0]==n:
#                         p=input("enter the author")
#                         i[2]=p
#                         print("authorupdated")
#             if c==3:
#                 for i in main:
#                     if i[0]==n:
#                         p=input("enter the price")
#                         i[3]=p
#                         print("price updated")
#
#             if c==4:
#                 for i in main:
#                     if i[0]==n:
#                         p=input("enter the publishers")
#                         i[4]=p
#                         print("publishers updated")
d={}
while True:
    print("1.created")
    print("2.delete")
    print("3.update")
    print("4.display")
    f=int(input("Enter the choice:"))
    if f==1:
        a=int(input("Enter the range:"))
        for i in range(a):
            k=int(input("Enter the key:"))
            y=input("Enter the value:")
            d.update({k:y})
            print("The book created")
    elif f==2:
            b=int(input("enter the key:"))
            if b in d:
                d.pop(b)
                print("dictionary is deleted")
    elif f==3:
            c=int(input("Enter the key:"))
            if c in d:
                h=int(input("Enter the value"))
                print(h)
                d[c]=h
                print("updated")
    elif f==4:
            print(d)



