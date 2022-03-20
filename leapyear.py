def isLeap(year):
    leap =False
    if year % 400 == 0  or year % 4 == 0 and year % 100 !=0 :
        leap = True
    else:
        leap = False
    return leap
print("plz! Enter year")
year = int(input())
print(isLeap(year))
