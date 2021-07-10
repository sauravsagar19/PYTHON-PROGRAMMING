def is_leap(year):
    if year % 400 == 0:
        print("True")
    if year % 100 == 0:
        print("False")
    if year % 4 == 0:
        print("True")
    else:
        print("False")
