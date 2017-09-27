from .parsning import searchWords
import time

dirToJson = '../data/'
wordToFind = [['han', 0], ['hon', 0], ['den', 0], ['det',0], ['denna',0], ['denne', 0], ['hen',0]]

def addWordCount(listAddTo, listAddFrom):


    return

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
        if i > 10:
            break

print wordToFind
