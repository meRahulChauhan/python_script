class demo2:

    def __init__(self):
        self.a=103
        self.b=97
        self.c=-2     #initialization of Instancevariable
        self.d=100
        self.e=20
    def display(self):
        #del self.c    #deletion of Instancevariable
        print(self.a)
        print(self.b)
        print("Addition of %s+%s=%s" %(self.a,self.b,self.a+self.b))
    def deletionMethod(self):
        del self.c #comment this line using hash before del to see the effects and revive Instancevariable 'c'
        del self.e #comment this line using hash before del to see the effects and revive Instancevariable 'e'
        print("Instancevariable 'c' & 'e' deleted successfully")#del self.c    #deletion of Instancevariable
OBJ=demo2()
OBJ.display()
print("a: ",OBJ.a)
print("b: ",OBJ.b)
print("c: ",OBJ.c)   #working  since c is available
print(OBJ.__dict__)  #{'a': 103, 'b': 97, 'c': -2, 'd': 100, 'e': 20}
OBJ.deletionMethod() #Instancevariable 'c' & 'e' deleted successfully
print(OBJ.__dict__)  #{'a': 103, 'b': 97, 'd': 100}

print()
# print("c: ",OBJ.c) won't work since c is deleted

#UPDATING DATA UNDER CLASS IN Instancevariable
OBJ2=demo2()
OBJ2.a='xyz'
OBJ2.b="ballPen"
OBJ2.c="cat"
OBJ2.d="DiskError"
OBJ2.e="Elephant"
OBJ2.display()        # a=xyz, b=ballpen, a+b=Addition of xyz+ballPen=xyzballPen
print(OBJ2.__dict__)  #{'a': 'xyz', 'b': 'ballPen', 'c': 'cat', 'd': 'DiskError', 'e': 'Elephant'}
OBJ2.deletionMethod() #Instancevariable 'c' & 'e' deleted successfully
print(OBJ2.__dict__)  #{'a': 'xyz', 'b': 'ballPen', 'd': 'DiskError'}
