"""rng=range(0,-1000,-30)
print(rng)
for y in rng:
    print(y)
    """
lst =["apple","list","tuple","set","frozenset",1,2,2,4,4,3,4,5,6.789,"Last Index"]
print(lst)
print(id(lst))
print(type(lst))
lst[0]="banana"
lst.append("root")
lst.append("rahul")
lst.append("chauhan")
lst.append("Impurities")
lst.remove("Impurities")
print(lst)
listlength =len(lst)
print(listlength)
print(lst[listlength-1].upper())
print(id(lst))

"""tp=("apple","list","tuple","set","frozenset",1,2,3,2,4,4,4,5,6.789)
print(tp)
print(type(tp))"""



lst =("apple","list","tuple","set","frozenset",1,2,2,2,2,2,4,4,3,4,5,6.789,"Last Index")
print(type(lst))
print(lst)
print(id(lst))

# lst[0]="banana" tuple doesn't support item assignment 
# lst.append("root") tuple doesn't have append method
#lst.append("rahul")
#lst.append("chauhan")
#$lst.append("Impurities")
#lst.add("Impurities") Immutable no operation can be performed after creating tuple 
print(lst)
listlength =len(lst)
print(listlength)
print(lst[listlength-1].upper())
print(id(lst))
print(lst.count(2))
print(lst.index(2))




st={"apple","list","tuple","set","frozenset",1,2,2,4,4,3,4,5,6.789,"Last Index"}
print(type(st))
print(id(st))
print(st)
print(st.clear()) # clears entire set  : None
del st # deletes entire set
st={"blank"} #Empty set : {}
print(st)
print(id(st))
st={"apple","list","tuple","set","frozenset",1,2,2,4,4,3,4,5,6.789,"Last Index"}
st.add("16")
st.add("Impurities")
st.add("Impurities")
st.add("INR")
st.add("USD")
print(st)
st.remove("Impurities")
st.discard("USD")
print(len(st))
print(st)
print(id(st))
"""for y in st:
    print(y)"""

set1={"ubuntu","Linux Mint","Debian","Kali","BlackArch","Ubuntu Server","Fedora","Manjaro","Arch","Parrot","Android"}
set2={"Window 3","Window XP","Window 7","Window 8","Window 8.1","Window 10","Window 11","Window server 2012"}
set3={"TCL/tl","C","C++","C#","SmallTalk","Ruby","Java","Python","PHP","Perl","Javascript","ASPX","CLISP",}
print(id(set1))
print(type(set1))
print(len(set1))

print(id(set2))
print(type(set2))
print(len(set2))

print(id(set3))
print(type(set3))
print(len(set3))

setlist=set1.union(set2).union(set3)
for y in setlist :
    print(y)
    
