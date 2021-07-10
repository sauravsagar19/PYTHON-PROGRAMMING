smallest=None
for i in [10,11,13,9,23,45]:
    if smallest is None:
        smallest=i
    elif i<smallest:
        smallest=i
print(smallest)
