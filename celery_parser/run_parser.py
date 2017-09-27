from .parsning import searchWords
import os, json, urllib, copy, re, time

dirToJson = 'data/'
wordToFind = [['han', 0], ['hon', 0], ['den', 0], ['det',0], ['denna',0], ['denne', 0], ['hen',0]]

def getFiles(dirToJson):

    try:
        filesInDir = os.listdir(dirToJson)
        return filesInDir
    except Exception as e:
        print e

    return []

def addWordCount(listAddTo, listAddFrom):
    i = 0
    for e in listAddTo:
        print "-------------------------------------------------"
        print listAddTo[i][1], " + ", listAddFrom[i][1], " = ", listAddTo[i][1] + listAddFrom[i][1]
        listAddTo[i][1] += listAddFrom[i][1]
        print listAddTo[i][1]
        print "-------------------------------------------------"
        i += 1


    return listAddTo

if __name__ == '__main__':
    print "starting to search in folder "+dirToJson
    files = getFiles(dirToJson)
    listWithInstances = []
    #adds all active instances to list
    print 'found ', len(files),  ' in that folder'
    for f in files:
        wordToFind_c = copy.deepcopy(wordToFind)
        if f[0] != '.':
              listWithInstances.append(searchWords.delay(wordToFind_c, dirToJson+f))

    i = 0
    print wordToFind_c
    while len(listWithInstances) != 0:
        for instance in listWithInstances:
            if instance.ready():
                print instance.result
                addWordCount(wordToFind, instance.result)
                listWithInstances.remove(instance)
        time.sleep(2)
        i += 1
        if i > 40:
            print 'avbruten exe'
            break

print wordToFind
