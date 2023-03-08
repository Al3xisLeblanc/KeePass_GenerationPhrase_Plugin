import spacy
import sys
import os


def spacyLibraryFromCode(languageCode:str):

    switch = {
        "fr":"fr_core_news_sm",
        "en":"en_core_web_sm"
    }
    return switch.get(languageCode)
    
def generateDictionnaryFiles(languageCode:str):

    dictionnaryFolders = DICTIONNARIES_FOLDER_PATH + "dictionnary_" + languageCode + "/"
    os.mkdir(dictionnaryFolders)
    
    files ={
        "ADP" : open(dictionnaryFolders+"ADP.txt", "w+"),
        "DET" : open(dictionnaryFolders+"DET.txt", "w+"),
        "NOUN" : open(dictionnaryFolders+"NOUN.txt", "w+"),
        "DET" : open(dictionnaryFolders+"DET.txt", "w+"),
        "VERB" : open(dictionnaryFolders+"VERB.txt", "w+"),
        "AUX" : open(dictionnaryFolders+"AUX.txt", "w+"),
        "PROPN" : open(dictionnaryFolders+"PROPN.txt", "w+")
    }
    return files


def main(wordListFile:str, languageCode:str):
    nlp = spacy.load(spacyLibraryFromCode(languageCode))

    if not os.path.isfile(wordListFile):
        raise Exception("Ce chemin du fichier de mots est invalide: " + wordListFile)

    dictionnary = open(wordListFile,'r')
    words = dictionnary.read()
    dictionnary.close()

    tokens = nlp(words)
    generateDictionnaryFiles(languageCode)
    
    for token in tokens:
        if token.pos_ == "X":
            print(token)

    


if __name__ == "__main__":

    DICTIONNARIES_FOLDER_PATH = "./Dictionnaries/"
    main(sys.argv[1], sys.argv[2])