# f=open("file.name",'r')
# print(f.read())
# with open("file.name",'r') as f:
#     print(f.read())
# f=open("text.txt",'x')
# f.close()
# f=open("text.txt",'w')
# f.write("how are you\n")
# f.close()
# f=open("text.txt",'a')
# f.write("Helloworld")
# # f.close()
# f=open("text.txt",'r')
# # print(f.readlines())
# x=f.readlines()
# print(x[0])
# f=open("file.name",'r')
# y=f.read()
# for i in y:
#     print(i)
# import os
# os.remove("file.name")
# print("file removal")
# import os
# if os.path.exists("file.name"):
#     os.remove("file.name")
#     print("file removed")
# else:
#     print("file not found")
# f=open("text.txt",'r')
# print(f.read())
# print(f.tell())
# f.seek(1)
# print(f.tell())
# f=open("text.txt",'r')
# x=f.read()
# for i in enumerate(x):
#     print(i)
f=open("text.txt",'r')
f1=open("ket.txt",'w')
for i in f:
    f1.write(i)