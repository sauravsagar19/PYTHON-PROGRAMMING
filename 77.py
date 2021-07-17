list=[]
ls1=input("enter guest 1")
list.append(ls1)
ls2=input("enter guest 2")
list.append(ls2)
ls3=input("enter guest 3")
list.append(ls3)
print(list)
n=(input("write the name "))
if n in list:
    c=input("want to invite?(y/n)")
    if c=="y":
        print("okkay your final list is:",list,"having total",len(list),"member")
    elif c=="n":

        print(list.index(n))
#        list=list.remove(n)
#        print(list)
else:
    print("not in list")
