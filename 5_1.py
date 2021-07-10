counts=dict()
open=input("enter sentence ")
line=open.split()
print(line)
for word in line:
     counts[word]=counts.get(word,0)+1
print(counts)
bigword=none
bigcount=none
for word,line in counts.items():
    if bigcount is none or line>bigcount:
        bigword=word
        bigcount=line
print(bigword,bigcount)
