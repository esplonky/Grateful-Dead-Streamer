from internetarchive import *
import json
import xml.etree.ElementTree as ET
import random
import time
import os.path



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
        m = open('gdshowtitles.json', 'w')
        metaDict = {0: {}}

        for i in f:
            metaDict[x] = f
            metaDictRoot = metaDict[x]
            encodeJSON = json.dumps(i)
            metaDictEncode = encodeJSON

            m.write(metaDictEncode)
           # print metaDict[x]
            print metaDictEncode
            x+=1
        return metaDict



def loadJsonFromGDFile():

    with open('gdshowtitlelist.json') as json_data:
        f = json.load(json_data)
        json_data.close()
        return(f)




def makeShowLink():
    tree = ET.parse('gdshowtitlelist.xml')
    root = tree.getroot()
    showlist = []
    for i in tree.findall('shows/identifier'):
        #print i.text
        identifierToLink = "https://archive.org/d/" + i.text
        showlist.append(identifierToLink)
    return showlist

def getShowMetaData():
    f = open('gdshowIDs.txt', 'r')
    h = open('gdShowInternalMeta', 'w')
    idBuffer = makeShowLink()
    for i in idBuffer:
        showIdentifierMeta = get_item(i)
        metadata = showIdentifierMeta.metadata
        print metadata

getShhowMetaData()


       # metadataFilesStg = showIdentifierMeta.metadata['files']

        #metacombine = metadataIdentifierStg + ', ' + metadataTitleStg + ', ' + metadataYearStg + ', ' + metadataTrackListStg + ', ' + metadataFilesStg
        #metawrite = str(metadataStg) + '\n'
        #h.write(metawrite)


