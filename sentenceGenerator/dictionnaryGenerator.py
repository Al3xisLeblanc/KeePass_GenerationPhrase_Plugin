import spacy
import sys
import os


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
    for fileName in files: os.remove(folderPath+fileName)


def generateDictionnaryFiles(languageCode:str):

    positions = ["ADJ", "ADP", "ADV", "AUX", "CONJ","CCONJ", "DET", "INTJ", "NOUN", "NUM", "PART", "PRON", "PROPN", "PUNCT", "SCONJ", "SYM", "VERB", "X"]

    dictionnaryFolder = DICTIONNARIES_FOLDER_PATH + "dictionnary_" + languageCode + "/"
    if not os.path.exists(dictionnaryFolder): os.mkdir(dictionnaryFolder)
    else: emptyFolder(dictionnaryFolder)
    
    files = {}
    for pos in positions: files[pos] = open(dictionnaryFolder + pos + ".txt", "w+")
    return files


def main(wordListFile:str, languageCode:str):
    nlp = spacy.load(spacyLibraryFromCode(languageCode))

    if not os.path.isfile(wordListFile):
        raise Exception("Ce chemin du fichier de mots est invalide: " + wordListFile)

    dictionnary = open(wordListFile,'r')
    words = dictionnary.read()
    dictionnary.close()

    tokens = nlp(words)
    wordPositionFiles = generateDictionnaryFiles(languageCode)
    
    nbTokenX= 0
    for token in tokens:
        
        if token.pos_ != 'SPACE' and token.pos_ !='PUNCT':
            wordPositionFiles[token.pos_].write(token.lemma_ + "\n")
    

if __name__ == "__main__":

    DICTIONNARIES_FOLDER_PATH = "./Dictionnaries/"
    args = sys.argv[1:]
    if len(args) < 2: raise Exception("2 parameters required: \n1. Word list file path \n2.Language code")
    main(sys.argv[1], sys.argv[2])