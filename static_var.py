class root:
    a='10' #static variable a best place to declare is begin of class
    def __init__(self):
        self.a=10
        self.b=20
OBJ=root()
print("Instance variable: ",OBJ.__dict__)
print("Class dictionary: ",root.__dict__)
for x in OBJ.__dict__:
    print(x)
for y in root.__dict__:
    print(y)

print("class root1")

class root1:
    '''Declaration of static variable inside the instanceMethod '''
    a='10' #static variable a best place to declare is begin of class
    name="rahulchauhan"
    def __init__(self):
        self.a=10 #Instancevariable
        self.b=20
        self.c=30
        root1.c=100
        root1.name1="savitaChauhan"
    def fx(self):
        self.os="Ubuntu"   #won't work until instanceMethod is called
        root1.user="savirc"
    @classmethod
    def classmethodfx(cls):
        cls.password="qwerty123"
        cls.alg="AES128"
        root1.key="NO_KEY"

OBJ2=root1()
OBJ2.fx()
print("Instance variable: ",OBJ2.__dict__)
print("Class dictionary: ",root1.__dict__)
print()
print("object 3")
OBJ3=root1()
OBJ3.fx()
OBJ3.classmethodfx()
print("Instancevariable: ",OBJ3.__dict__)
print("class static variable: ",root1.__dict__)
#for x in OBJ2.__dict__:
#    print(x)
#for y in root1.__dict__:
#    print(y)
