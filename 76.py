list=[]
ls1=input("enter guest 1")
list.append(ls1)
ls2=input("enter guest 2")
list.append(ls2)
ls3=input("enter guest 3")
list.append(ls3)
print(list)
conf=input("anyone more?")
while conf=="yes":
    newname=list.append(input("enter the name"))
    conf=input("anyone else?")
    print(list)
