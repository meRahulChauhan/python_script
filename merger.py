from sys import argv
name=input("Name the output file: ")
filename=open(name,"w")
a=range(1,len(argv))
for x in a:
    file =open(argv[x])
    for y in file:
        filename.write(y)
for x in a:
    print(argv[x]+ " written successfuly to "+name,x,"of",len(argv)-1,"done ")
print(len(argv)-1,"file successfully merged to",name)
