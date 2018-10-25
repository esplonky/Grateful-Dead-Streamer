from internetarchive import *
import json

def getListOfDeadShows():

    #Search for all things groovy
    listShowsJSON = search_items('collection:(GratefulDead)')

    #Couple of containers for some JSON data containing show's unique ID's
    listShowsStripped = []
    listShowsDecoded = []

#Decode and Store the JSON Data to be used later
    for a in listShowsJSON:
        listShowsBuffer = json.dumps(str(a))
        listShowsDecoded.append(listShowsBuffer)
    for i in listShowsDecoded:
        noU = str(i).replace('"{u\'identifier\': u\'', '')
        noEnd = str(noU).replace('\'}\"', '')
        listShowsStripped.append(noEnd)
    return listShowsStripped

def getShowTitle():
    showList = getListOfDeadShows()
    showID = []
    for i in showList:
        showID.append(i)
    print showID
    return showID

def selectShow():
    showList = getShowTitle()
    searchQuery = str(raw_input("Enter a query: "))
    x = 0
    searchResults = {}
    for i in showList:

        if searchQuery in i:
            searchStg = str(x) + ' ' + i
            print searchStg
            searchResults[x] = {'showID': i}
            x += 1
    showQuery = input("Choose a show: ")
    return searchResults[showQuery]


def getShowMeta():
    showID = selectShow()
    showsStg = {}
    setlistStg = {0: {}}
    noBraces = str(showID).replace('{\'showID\': \'', '')
    noEnd = noBraces.replace('\'}', '')

    f = open('showsStgFile', 'w')
    item = get_item(noEnd)
    files = get_files(noEnd)
    x = 0
    for i in files:
        setlistStg[x] = i
        x += 1
    allMeta = item.metadata
    showsStg = allMeta
    f.write(str(showsStg) + '\n')
    f.close()
    titleOfShow = showsStg['title']
    subjectOfShow = showsStg['subject']
    yearOfShow = showsStg['year']
    print titleOfShow + '\n' + subjectOfShow + '\n' + yearOfShow + '\n'
    for a in setlistStg:
        print setlistStg[a]
   # print showID
   # print noEnd
   # print showsStg
getShowMeta()