class pyBank:
    '''Python banking app'''
    bankName="pyBank"
    def __init__(self,name,bal=0.0):
        self.name=name
        self.bal=bal
    def deposit(self,amount):
        self.amount=amount
        if self.amount<=0:
            print("Negative or zero bal can'be added to account , kindly try again")
            print("Available bal: ",self.bal)
        else:
            self.bal=self.bal+self.amount
            print(self.amount," deposited to account successfully ")
            #print("Available bal:",self.bal)
    def withdraw(self,amount):
        self.amount=abs(amount)
        if self.bal < self.amount:
            print("Insufficient balance , add %s more to withdrew amount of %s" %(abs(self.bal-self.amount),self.amount))
        else:
            self.bal=self.bal-self.amount
            print(self.amount," withdrawn successfully ")
            print("Available bal: ",self.bal)
name=input("Enter name: ")
bank=pyBank(name)
#print(bank.name)
print("Hi '%s' welcome to '%s' application" %(bank.name,pyBank.bankName))
while True:

    opt=input("kindly select options below\n\tbal : Check balance\n\td : deposit\n\tw : withdraw\n\te : exit\n\tyour selection: ")
    opt=opt.strip()
    if opt.lower()=='d':
        amount=float(input("\tEnter deposit amount: "))
        bank.deposit(amount)
    elif opt.lower()=='bal':
        print("Available Amount: ",bank.bal)
    elif opt.lower()=='w':
        amount=float(input("\tEnter withdraw amount: "))
        bank.withdraw(amount)
    elif opt.lower()=='e' or opt.lower()=='exit' :
        print("\tThanks for using pyBank app:  ")
        print("\tExiting ....")
        break
    else :
        print("choose a valid option ")
