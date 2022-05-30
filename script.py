name="rAHUl" # print string /type str
print(name[0:5]) # slice 0-(5-1) 
r=name # assigns name str type value to variable r
print(r) # print r 
r1=r[-5].upper()+r[1:5].lower() # print first value to smaalcase and other in uppercase
print(r1) # output -> rAHUL
r=20+10j  #complex number 
r0=30-60j # complex number
print(r*r0) #  multiplicvation of of both complex number
txt="sAnToSh kuMAR SharMA" 
txt=txt[0].upper()+txt[1:len(txt)].lower() # O index at uppercase,  All  character start from 1 index will be in small case
print(txt)
txt1="aakskrkekrkhhdtckrgjcgjrkjgkjtrgckjgtkjcgctr" 
#H last letter should be capital
txt1=txt1[0:len(txt1)-1]+txt1[-1].upper()
print(txt1)
print(len(txt1))
print(len(txt))
txt2="camel" 
#AsrfkejncA
txt2=txt2[0].upper()+txt2[1:len(txt2)-1]+txt2[len(txt2)-1].upper()
print(txt2)
txt2="camel"
print(txt2)
print(txt2[0])
print(len(txt2))
print(len(txt2)-1)
print(txt2[4])
