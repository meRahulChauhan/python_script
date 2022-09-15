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
