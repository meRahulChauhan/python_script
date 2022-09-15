num=int(input("Enter Number "))
file_name=input("Enter Filename ")
file=open(file_name,'w',encoding='ISO-8859-1')
pnum=snum=num
print("You Entered %i" %num)
r=range(len(str(num)))
i=len(str(num))-1
b=0
s=9
n=0
for x in r:
    if(num%10>b):
        b=num%10
        num=num//10
    else:
        num=num//10
print("Biggest digit in %i is %i" %(pnum,b))
for x in r:
    if (snum%10<s) :
        s=snum%10
        snum=snum//10
    else:
        snum=snum//10
print("Smallest digit in %i is %i" %(pnum,s))
multiple_of_ten=10**i
print(multiple_of_ten)
for x in range(0,i+1):
    multi=multiple_of_ten*b
    #print(multi)
    n=n+multi
    multiple_of_ten=multiple_of_ten//10
    #print(multiple_of_ten)
print("Possible mini number %i"%s)
print("Possible max number %i"%n)
for x in range(s,n+1):
    x=str(x)+"\n"
    file.write(x)
