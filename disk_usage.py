import os
def disk_usage(path):
    total=os.path.getsize(path)
    if os.path.isdir(path):
        for file in os.listdir(path):
            childpath=os.path.join(path,file)
            total+=disk_usage(childpath)
    if total >1048576:
        print('{0:<7}MB'.format(total//1048576),path)
        return total
    elif total >1024:
        print('{0:<7}KB'.format(total//1024),path)
        return total
    elif total <1024:
        print('{0:<7}B'.format(total),path)
        return total

path=input("Enter directory name: ").title()
x=disk_usage(path)
if x<1024:
    print(x,"B used")
elif x<1048576:
    print(x//1024,"KB used")
elif x>1048576 :
    print(x//1048576,"MB used")
