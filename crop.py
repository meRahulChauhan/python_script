class crop:
    def __init__(self,crop,season,water,height,yeild):
        self.crop=crop
        self.season=season
        self.water=water
        self.height=height
        self.yeild=yeild
    def info(self):
        print("\t%s is a %s crop , requires  %s of water. grow upto %s and a  %s"%(self.crop,self.season,self.water,self.height,self.yeild))
obj1=crop("Rice","rainy","40-110cm","1.6m","High Yeilding variety")
obj1.info()
obj2=crop("Mango","Tropical","50cm","30m","High Yielding variety")
obj2.info()
