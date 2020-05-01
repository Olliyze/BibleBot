import math
import os
import json
import sys

class verseID:
    def __init__(verseObject, bookAbbr, chapter, verseNum):
        verseObject.bookAbbr = bookAbbr
        verseObject.chapter = chapter
        verseObject.verseNum = verseNum

verseList = [] #should be accessible from outside of py file

def addVersesToList(abbr, chap, verseNumberString):
    for x in range(1, int(verseNumberString)+1):
        y = verseID(abbr, chap, x)
        verseList.append(y)
    return

#load up the verse counts to initialize corresponding api request/random number ranges
def returnArrayOfVerse():

    with open('qbiblebot/verse count.json', 'r') as fp:
        obj = json.load(fp)

        for i in obj:
            tempAbbr = i['abbr']
            tempCounter = 0
            for j in i['chapters']:
                tempChapNum = j['chapter']
                tempNumVerses = j['verses']
                addVersesToList(tempAbbr, tempChapNum, tempNumVerses)

    return verseList

# testArr = returnArrayOfVerse()
# for m in testArr:
#     print(m.bookAbbr + str(m.chapter) + "-" + str(m.verseNum))