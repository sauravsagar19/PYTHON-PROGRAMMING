certificate="This is to certify that saurav_has_done_very_well in python classes."
search=certificate.find("saurav")
print(search)
searchnxt=certificate.find(" ",search)
print(searchnxt)
cutout=certificate[search:searchnxt]
print(cutout)
