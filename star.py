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
