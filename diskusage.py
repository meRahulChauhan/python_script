#!/bin/python3.10
import os
def disk_usage(path):
    total=os.path.getsize(path)
    mb=int(total/(1024*1024))
    kbytes =int(total/1024)
    if os.path.isdir(path):
        for file in os.listdir(path):
            childpath=os.path.join(path,file)
            total+=disk_usage(childpath)
    if os.path.getsize(path)>1048576:
        print('{0:<7} MB '.format(mb),path)
        return total
    elif os.path.getsize(path)<1048:
        print('{0:<7} Bytes '.format(total),path)
        return total
    else:
        print('{0:<7} KB '.format(kbytes),path)
        return total
    return total
path=input("Enter folder name: ").title()
x=disk_usage(path)
#print(x)
if x<1024:
    print(x,"Bytes  used")
elif x<1048576:
    print(x/1024,"KBytes used")
elif x>1048576 :
    print(x/1048576,"MBytes  used")
