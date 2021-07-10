f=input("enter name of file")
try:
    fhand=f.open(f)
except:
    print(f," file can't be open")
    quit()
count=0
for line in fhand:
    if line.startswith("with"):
        count=count+1
print("there were",count,"in the file",f)
