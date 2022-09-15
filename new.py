from sys import argv
""" a=int(argv[1])
b=int(argv[02])
c=int(argv[03])
print(a+b+c) """
num=0
a=len(argv)
b=range(1,a)
for x in b :
        num=num+int(argv[x])
print(num)
S1="rahul"
print(S1)
print("Enter A's value")
a=input()
print("Enter B's value")
b=input()
if a>b :
    print("A is Greater than B")
if b>a :
        print("B is Greater than A ")
if b==a :
        print("Both Values  Are Equal ")
a=chr(97)
b=ord("A")
print(a)
print(b)
a=0b011101100
print(a)
b=0xdac
print(b)
b=0xfade
print(b)
b=0xbad
print(b)
b=0xbade
print(b)
b=0xbadda
print(b)
b=0xbac12303451
print(b)
b=0xba01b232e
print(b)
b=0o4000
print(b)
print(type(b))
print(type(b))
b=1024
print("Decimal "+str(b))
b=hex(b)
print("Hexadecimal "+str(b))
print(type(b))
b=1024
b=bin(b)
print("Binary "+str(b))
print(type(b))
b=1024
b=oct(b)
print("Octal "+str(b))
print(type(b))
