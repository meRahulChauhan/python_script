num=(int)(input("Enter Number: "))
print(num)
z=len(str(num))
print(z)
y=0
for x in range(z):
    print(x)
    if(num%10>y):
        y=num%10
        print(y)
        num=num//10   
        print(num)  
    else:
       num=num//10 
       print(num)  
print(y)
'''
num=int(input("Enter any Number : "))
min=9
while num>0:
    digit=num%10
    if min>digit:
        min=digit
    num=num//10
print("Smallest Digit is : ",min)'''
