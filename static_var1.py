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
root1.phone3="9219011866"
print("Class level variable: ",root1.__dict__)
