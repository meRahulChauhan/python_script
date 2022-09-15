class student:
    ''''Doc String'''
    def __init__(self):
        self.name="rahul"
        self.phone="8127006993"
        self.os="Ubuntu"
    def talk(self):
        print("My name is ",self.name)
        print("My OS is   ",self.os)
        print("My phone number is ",self.phone)
referenceVariable=student()
print(referenceVariable.name)
print(referenceVariable.os)
print(referenceVariable.phone)
