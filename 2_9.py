certificate="This is to certify that saurav has done very well in python classes."
search=certificate.find("saurav")
print("position of saurav is",search)
searchnxt=certificate.find("in",search)
print("position of well is",searchnxt)
cutout=certificate[search:searchnxt]
print("cutting out the sentence between position no",search,"and",searchnxt," and the sentence is",cutout)
