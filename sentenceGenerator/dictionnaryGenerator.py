import spacy
from languageProcessors import SpacyProcessor
import sys
import os
import shutil
from dictionary import Dictionary
from icecream import ic


def spacyLibraryFromCode(languageCode:str):

    switch = {
        "fr":"fr_core_news_sm",
        "en":"en_core_web_sm"
    }
    return switch.get(languageCode)
    
def emptyFolder(folderPath):

    if not os.path.exists(folderPath): return None

    files = os.listdir(folderPath)
    print(files)
    for fileName in files: 
        
        filePath = folderPath+fileName
        if os.path.isdir(filePath): shutil.rmtree(filePath)
            # emptyFolder(filePath)
            # os.rmdir(filePath)
        else: os.remove(filePath)




def generateDictionnaryFiles(dictionnaryFolder:str):

    positions = ["ADJ", "ADP", "ADV", "AUX", "CONJ","CCONJ", "DET", "INTJ", "NOUN", "NUM", "PART", "PRON", "PROPN", "PUNCT", "SCONJ", "SYM", "VERB", "X"]

    if not os.path.exists(dictionnaryFolder): os.mkdir(dictionnaryFolder)
    else: emptyFolder(dictionnaryFolder)
    
    positionFolders = {}
    for pos in positions: positionFolders[pos] = os.mkdir(dictionnaryFolder + pos)
    return positionFolders


def processDictionnary(wordListFile:str, languageCode:str):
    nlp = spacy.load(spacyLibraryFromCode(languageCode))

    if not os.path.isfile(wordListFile):
        raise Exception("Ce chemin du fichier de mots est invalide: " + wordListFile)

    dictionnary = open(wordListFile,'r')
    words = dictionnary.read()
    dictionnary.close()

    tokens = nlp(words)
    dictionnaryFolder = DICTIONNARIES_FOLDER_PATH + "dictionnary_" + languageCode + "/"
    wordPositionFiles = generateDictionnaryFiles(dictionnaryFolder)
    stemFiles = []
    
    for token in tokens:
        
        if token.pos_ != 'SPACE' and token.pos_ !='PUNCT':

            
            stemFile = nltk.stem(token.lemma) + ".txt"
            if not stemFiles[stemFile]:
                stemFiles[stemFile] = open(dictionnaryFolder+token.pos_+ stemFile, "a+")

            stemFiles[stemFile]
            wordPositionFiles[token.pos_].write(token.lemma + "\n")

# def generateDictionary(wordListFile, nlp: SpacyProcessor):
#     dict = []
#     with open(wordListFile, 'r') as file:
#         words = file.read()

#     tokenisedWords = nlp.tokenise(words)
#     for token in tokenisedWords:
#         if not token.position == 'SPACE':
#             dict.append({"word": token.word, "stem": token.stem, "position": token.position})
#     return dict

def generateDictionary(wordListFile, languageCode: str, dictionarySaveFolder:str):
    nlp = SpacyProcessor(languageCode)
    dict = Dictionary("basicEnglishDictionary", languageCode, dictionarySaveFolder)
    with open(wordListFile, 'r') as file:
        words = file.read()

    tokenisedWords = nlp.tokenise(words)
    for token in tokenisedWords:
        if not token.position == 'SPACE':
            dict.addWord(str(token.word), token.stem, token.position)
    return dict
    
def generateTestDictionary():
    dict = []
    dict.append({"word":"will", "stem":"will","pos": "AUX"})
    dict.append({"word":"will", "stem":"will","pos": "NOUN"})
    return dict




if __name__ == "__main__":

    DICTIONNARY_FILE_PATH = "./wordLists/liste_francais.txt"
    DICTIONNARIES_SAVE_FOLDER = "./Dictionnaries/"
    args = sys.argv[1:]
    
    #words = args[0]
    #tokenisedWords = nlp.tokenise(words)
    dictionary = generateDictionary(DICTIONNARY_FILE_PATH, "fr", DICTIONNARIES_SAVE_FOLDER)
    dictionary.save()
    #dictionary.save()
    #dictionary = generateTestDictionary()

    
    

    # for token in tokenisedWords:
    #     #print([token.word, token.stem, token.position])
    #     ic(token)

    #     dict.append(Word(token.word, token.stem, token.position))

    
    
    