import os, json, urllib, copy, re


dirToJson = '../data/'
wordToFind = [['han', 0], ['hon', 0], ['den', 0], ['det',0], ['denna',0], ['denne', 0], ['hen',0]]


def getFiles(dirToJson):
    try:
        filesInDir = os.listdir(dirToJson)
        return filesInDir
    except Exception as e:
        print('exeption: ----> ', e)

    return

def arrayHasWord(array, word):
    for element in array:
        if element == word:
            return True
    return False

def stringClean(string):
    stringNormalized = string.lower()
    stringE = re.sub('[^\w ]', ' ', stringNormalized, flags=re.UNICODE)
    stringSplit = stringE.split(' ')
    return stringSplit

def countWordsInString(wordsToSearch, string):
    stringPrepared = stringClean(string)
    for wordToFind in wordsToSearch:
        if arrayHasWord(stringPrepared, wordToFind[0]):
            wordToFind[1] += 1
    # print
    # print string
    # print wordsToSearch
    # print

    return wordsToSearch

def searchWords(wordsToSearch, patToFile):
    i = 1
    fileStream = open(patToFile, 'r')
    try:
        with fileStream as openFile:
            for line in openFile:
                if line != '\n':
                    parsedJson = json.loads(line)
                    if not parsedJson.has_key('retweeted_status'):
                        stringToAnalyze = parsedJson['text']
                        wordsToSearch = countWordsInString(wordsToSearch, stringToAnalyze)


                    # i += 1
                    # if i > 2000:
                    #     print 'raderna i filen klar ------->'
                    #     return wordsToSearch

    except Exception as e:
            print "problem i searchWords ---->", e
    finally:
        fileStream.close()

    return wordsToSearch


#---- main --->

files = getFiles(dirToJson)

for f in files:
    #wordToFind_c = copy.deepcopy(wordToFind)
    if f[0] != '.':
          resultat = searchWords(wordToFind, dirToJson+f)
          print resultat






#<------ end main -------
