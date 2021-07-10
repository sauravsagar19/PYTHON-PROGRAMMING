import urllib.request,urllib.parse,urllib.error
fhand=urllib.request.urlopen("file:///C:/Users/KIIT/Desktop/web%20tech/L2/New%20Text%20Document.html")
for line in fhand:
    print(line.decode().strip())
