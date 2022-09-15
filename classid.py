class classId:
    def __init__(self):
        print("\tid of constructer is: ",id(self));
    def auto(self,au):
        #print("ID of auto is: ",id(auto)) NOT DEFINED SO WON'T WORK
        print("\tvalue of au: ",au)
instanceVariable  =classId()
print("\tid of instanceVariable ",id(instanceVariable))
print("\tid of  instanceVariable ",instanceVariable)
obj1=classId()
obj1.auto("\tHEllo")
print("\tid of classId is: ",id(obj1))
