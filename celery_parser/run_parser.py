from .parsning import searchWords
import os, json, urllib, copy, re, time

dirToJson = 'data/'
wordToFind = [['han', 0], ['hon', 0], ['den', 0], ['det',0], ['denna',0], ['denne', 0], ['hen',0]]

def getFiles(dirToJson):

    try:
        print os.listdir('.')
        filesInDir = os.listdir(dirToJson)
        return filesInDir
    except Exception as e:
        print e

    return []

def addWordCount(listAddTo, listAddFrom):
    i = 0
    for e in listAddTo:
        listAddTo[i][1] += listAddFrom[i][1]
        i += 1


    return listAddTo

if __name__ == '__main__':

    files = getFiles(dirToJson)
    listWithInstances = []
    #adds all active instances to list
    for f in files:
        wordToFind_c = copy.deepcopy(wordToFind)
        if f[0] != '.':
              listWithInstances.append(searchWords.delay(wordToFind_c, dirToJson+f))

    i = 0
    while len(listWithInstances) != 0:
        for instance in listWithInstances:
            if instance.ready():
                addWordCount(wordToFind, instance.result)
                listWithInstances.remove(instance)
        time.sleep(2)
        i += 1
        if i > 40:
            break

print wordToFind
