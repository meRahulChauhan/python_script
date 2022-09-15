def gcd(a,b):
    assert int(a)==a and int(b)==b,"The number must be integer only"
    if a<0:
        a=-1*a
    if b<0:
        b=-1*b
    if b==0:
        return a
    return gcd(b,a%b)

a=eval(input("Enter a number: "))
b=eval(input("Enter other number: "))
gcd=gcd(a,b)
print(gcd)
