def chop(theList):
    length = len(theList)
    del theList[length-1]
    del theList[0]

tList = ['a','b','c','d']
chop(tList)
print(tList)
