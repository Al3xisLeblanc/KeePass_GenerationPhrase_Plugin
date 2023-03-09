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
    if not os.path.exists(dictionnaryFolders):
        os.mkdir(dictionnaryFolders)
    
    adpFile = dictionnaryFolders+"ADP.txt"
    detFile = dictionnaryFolders+"DET.txt"
    nounFile = dictionnaryFolders+"NOUN.txt"
    verbFile = dictionnaryFolders+"VERB.txt"
    auxFile = dictionnaryFolders+"AUXILIAIRE.txt"
    propnFile = dictionnaryFolders+"PROPN.txt"

    fileList = [adpFile, detFile, nounFile, verbFile, auxFile, propnFile]
    for file in fileList:
        if not os.path.exists(file):
            open(file, "x")

    

    files ={
        "ADP" : open(adpFile, "w"),
        "DET" : open(detFile, "w"),
        "NOUN" : open(nounFile, "w"),
        "VERB" : open(verbFile, "w"),
        "AUX" : open(auxFile, "w"),
        "PROPN" : open(propnFile, "w")
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
    #main(sys.argv[1], sys.argv[2])
    generateDictionnaryFiles(sys.argv[2])