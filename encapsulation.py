#public access
class A:
    name = "sajay"
    def display(self):
        print("Hello welcome")
        print(self.name)
obj=A()
obj.display()
print(obj.name)

class students:
    def __init__(self,name,rank,points):
        self.name = name
        self.rank = rank
        self.points = points
    def demofunc(self):
        print("I am ",self.name)
        print("I got rank",self.rank)
st1=students("steve",1,100)
st2=students("chris",2,98)
st3=students("Mark",3,76)
st4=students("kate",4,67)
st1.demofunc()
st2.demofunc()
st3.demofunc()
st4.demofunc()
private access
class A:
    __name = "sajay"
    def __display(self):
        print("Hello welcome")
        print(self.__name)
obj=A()
obj.display()
protected access
class A:
    _name = "sajay"
    def _display(self):
        print("Hello Welcome")
        print(self._name)
obj=A()
obj._display()
print(obj._name)