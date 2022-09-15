'''
Three types of method
class name:
name=rahulchauhan -> class method using @classmethod

    def __init__(self,name):
        self.name="rahul chauhan" # ->instance method

    def sum(a+b):
        return a+b -> static method
    def name(x):
        x="rahulchauhan"
        return x

         # cls is reference variable to which object? Everything is an OBJ in py3 even class also
         # for every class one class object is created to hold class level info
         # cls is a reference variable to class class OBJ to access class level info
         # No decorator used for Insatnce method
         Declaration of instance variable 3 ways to do
         1.Inside Constructor using self
         class demo1:
             def __init__(self):
                 self.x=10 #Instancevariable
                 self.y=20 #Instancevariable
         OBJ=demo()      # object created so, Instancevariable created   x=10,y=20
         print(OBJ.__dict__) # __dict__ is pre-defind variable to show Instancevariable Inside Constructor

         2.Inside Instance method using self
         class demo1:
             def __init__(self):
                 self.x=10 #Instancevariable
                 self.y=20 #Instancevariable
             def instanceMethod(self):
                 self.z=30
          OBJ=demo()          # object created so, Instancevariable created   x=10,y=20
          print(OBJ.__dict__) # __dict__ is pre-defind variable to show Instancevariable Inside Constructor

         3. Outside class by using OBJ reference variable
         pure code
         class demo1:
             def __init__(self):
                 self.x=10 #Instancevariable
                 self.y=20 #Instancevariable
             def instanceMethod(self):
                 self.z=30
                 self.a=40
         OBJ=demo1()         #object created so, Instancevariable created ,x=10,y=20  will be added to __dict__   in class
         OBJ.instanceMethod()#Instance called so z=30, a=40 added to __dict__ in class
         OBJ.b=50            # Declaration of Instancevariable b=50 Outside class and added to __dict_ in class
         print("\tdata in OBJ class",OBJ.__dict__) # __dict__ is pre-defind variable to show Instancevariable Inside Constructor [OBJ= x,y,x,a,b 10,20,30,40,50]
         OBJ2=demo1()
         OBJ2.instanceMethod()
         print("\tdata in OBJ2 class",OBJ2.__dict__) # [OBJ2 = x,y,x,a 10,20,30,40]
Story of static variable :
various place to declare static variable:
1.Within the class directly

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

2.Inside Constructor by using class name

class root:
    a='10' #static variable a best place to declare is begin of class
    def __init__(self):
        self.a=10 #Instancevariable
        self.b=20
        root.c=30
OBJ=root()
print("Instance variable: ",OBJ.__dict__)
print("Class dictionary: ",root.__dict__)
for x in OBJ.__dict__:
    print(x)
for y in root.__dict__:
    print(y)
3.Inside instanceMethod using class.variable name
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

OBJ2=root1()
OBJ2.fx()
print("Instance variable: ",OBJ2.__dict__) #Instance variable:  {'a': 10, 'b': 20, 'c': 30, 'os': 'Ubuntu'}
print("Class dictionary: ",root1.__dict__) #show all possible class dictionary

4.Inside classmethod using either cls variable or class name1

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
        cls.password="qwerty123"        #using cls variable
        cls.alg="AES128"                #using cls variable
        root1.key="NO_KEY"              #using class name variable

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

5.Inside Stati Method using class name1 [not by cls variable because cls is available only for classmethod]

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
        cls.password="qwerty123"        #using cls variable
        cls.alg="AES128"                #using cls variable
        root1.key="NO_KEY"              #using class name variable

    @staticmethod
    def staticmethodfx():
        root1.phone="7052461609"
        root1.phone2="8127006993"

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

print()

print("object 4")
OBJ4=root1()
OBJ4.fx()
OBJ4.classmethodfx()
OBJ4.staticmethodfx()
print("Instancevariable: ",OBJ4.__dict__)
print("Class level variable: ",root1.__dict__)

6.Outside class
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
        cls.password="qwerty123"        #using cls variable
        cls.alg="AES128"                #using cls variable
        root1.key="NO_KEY"              #using class name variable

    @staticmethod
    def staticmethodfx():
        root1.phone="7052461609"
        root1.phone2="8127006993"

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

print()

print("object 4")
OBJ4=root1
OBJ4.fx()
OBJ4.classmethodfx()
OBJ4.staticmethodfx()
print("Instancevariable: ",OBJ4.__dict__)
print("Class level variable: ",root1.__dict__)
OBJ4.phone3="9219011866"  # wrong approach
root1.phone3="9219011866" # outside the class using class.variable = value
print("Class level variable: ",root1.__dict__)
 '''

class methods:
    country ="India"  #static variable
    def __init__(self,name,id):
        self.name=name #instance variable
        self.id=id
        print("Constructor working ")
    def getInfo(self): #in instance method first argument is always self type
        print("id: %s, name: %s" %(self.id,self.name))  # Insatnce method

    @classmethod    #class method using class decorator
    def countryInfo(cls):
        print("Country Name: ", cls.country)
    #no instance , no class classmethod , general utility method
    @staticmethod #static method using staticmethod using decorator
    def showName():
        name="rahul chauhan"
        print(name)

obj1=methods('Rahul',12)
obj1.getInfo()
obj1.countryInfo()
obj1.showName()
