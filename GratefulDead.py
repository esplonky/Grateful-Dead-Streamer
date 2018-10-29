from internetarchive import *
import json
import xml
import time

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
        print i
    return showID

#def selectShow(searchQuery):

#    showList = getShowTitle()
#    x = 0
#    searchResults = {}

 #   for i in showList:

 #       if searchQuery in i:
   #         searchStg = str(x) + ' ' + i

 #           print searchStg

  #          searchResults[x] = {'showID': i}
  #          x += 1

 #   return searchResults[searchQuery]


def getShowMeta(showID):



    showsStg = {}
    setlistStg = {0: {}}

    noBraces = str(showID).replace('{\'showID\': \'', '')
    noEnd = noBraces.replace('\'}', '')

    item = get_item(noEnd)
    files = get_files(noEnd)

    x = 0

    for i in files:
        setlistStg[x] = i
        x += 1

    allMeta = item.metadata
    showsStg = allMeta


    titleOfShow = showsStg['title']
    #subjectOfShow = showsStg['subject']
    yearOfShow = showsStg['year']

    #print titleOfShow + '\n' + subjectOfShow + '\n' + yearOfShow + '\n'
    showMetaStg = [titleOfShow, yearOfShow]
    #print showMetaStg
    return showMetaStg
   # for a in setlistStg:
    #    print setlistStg[a]

def getShowMetaTitle():
    showIdBuffer = getShowTitle()
    showMetaBuffer = {0:{}}
    showTitleStg = []
    f = open('gdshowtitlelist', 'w')
    x = 0
    for i in showIdBuffer:
        noBraces = str(i).replace('{\'showID\': \'', '')
        noEnd = noBraces.replace('\'}', '')
        item = get_item(noEnd)

        itemMetaviewValues = item.metadata
        #titleMetaviewValues = itemMetaviewValues['title']


        print itemMetaviewValues
        #print titleMetaviewValues
        showMetaBuffer[x] = itemMetaviewValues
        #showTitleStg.append(titleMetaviewValues)

        f.write(str(showMetaBuffer[x]) + '\n')
        x += 1
    f.close()
    #return showTitleStg

def displayShowMeta():
    with open('noBraces') as f:
        fileLineStg = []
        x = 0
        m = open('gdshowdata', 'w')
        metaDict = {0: {}}

        for i in f:
            metaDict[x] = f
            metaDictRoot = metaDict[x]
            metaTitle = metaDictRoot[]
            encodeJSON = json.dumps(i)
            metaDictEncode = encodeJSON

            m.write(metaDictEncode)
           # print metaDict[x]
            print metaDictEncode
            x+=1
        return metaDict

displayShowMeta()