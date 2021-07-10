fhand=open("raja.txt")
for line in fhand:
    if line.startswith("hey: "):
        print(line)
    else:
        print("done")
