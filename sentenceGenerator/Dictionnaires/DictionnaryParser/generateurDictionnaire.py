import spacy
import sys


def spacyLibraryFromCode(languageCode:str):

    switch = {
        "fr":"fr_core_news_sm",
        "en":"en_core_web_sm"
    }
    return switch.get(languageCode)
    
def generateDictionnaryFiles(languageCode):

    dictionnaryFolders = "dictionnary_" + languageCode + "/"
    files ={
        "ADP" : open(dictionnaryFolders+"ADP"),
        "DET" : open(dictionnaryFolders+"DET"),
        "NOUN" : open(dictionnaryFolders+"NOUN"),
        "DET" : open(dictionnaryFolders+"DET"),
        "VERB" : open(dictionnaryFolders+"VERB"),
        "AUX" : open(dictionnaryFolders+"AUX"),
        "PROPN" : open(dictionnaryFolders+"PROPN")
    }
    return files
    
    

def main(dictionnaryFilePath:str, languageCode:str):
    nlp = spacy.load(spacyLibraryFromCode(languageCode))
    dictionnary = open(dictionnaryFilePath,'r')
    for word in dictionnary.readlines():
        print(word)

    


if __name__ == "__main__":

    main(sys.argv[1], sys.argv[2])