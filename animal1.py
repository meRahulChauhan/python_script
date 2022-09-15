class animal:
    '''Documentation string data'''
    def __init__(self,name,lifespan,weight,type):
        self.name=name
        #self.age=age
        self.lifespan=lifespan
        self.weight=weight
        self.type=type
    def auto(self):
        return("\t %s is a %s animal whose weight goes upto %s kg and lives upto %s years"
         %(self.name,self.type,self.weight,self.lifespan))
obj=animal("Dog","12","28","Domestic")
obj1=animal("Horse","28","400","Wild")
obj2=animal("Lion","25","250","Wild")
obj3=animal("Human","84","112","Social")
print(obj.auto())
print(obj1.auto())
print(obj2.auto())
print(obj3.auto())
