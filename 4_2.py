counts=dict()
sntce= input("enter sentence")
words=sntce.split()
print(words)
for word in words:
    counts[word]=counts.get(word,0)+1
print(counts)
