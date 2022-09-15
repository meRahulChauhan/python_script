class os1:
    def __init__(self,name,os,version):
        self.name=name
        self.os=os
        self.version=version
    def auto(self):
        print("I am using ",self.name,"OS")
        print("I am using ",self.os,"OS")
        print("I am using ",self.version,"version")
obj=os1("Linux","Ubuntu","22.04")
obj1=os1("Window","NT","20.04")
obj.auto()
obj1.auto()
