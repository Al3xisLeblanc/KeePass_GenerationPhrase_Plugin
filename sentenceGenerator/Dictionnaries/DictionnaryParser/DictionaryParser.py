import spacy
import sys


def spacyLibraryFromCode(languageCode:str):

    switch = {
        "fr":"fr_core_news_sm",
        "en":"en_core_web_sm"
    }
    return switch.get(languageCode)
    
def generateDictionaryFiles(outputDestination:str):

    dictionnaryFolders = outputDestination + "/"
    files ={
        "ADP" : open(dictionnaryFolders+"ADP", "w"),
        "DET" : open(dictionnaryFolders+"DET", "w"),
        "NOUN" : open(dictionnaryFolders+"NOUN", "w"),
        "DET" : open(dictionnaryFolders+"DET", "w"),
        "VERB" : open(dictionnaryFolders+"VERB", "w"),
        "AUX" : open(dictionnaryFolders+"AUX", "w"),
        "PROPN" : open(dictionnaryFolders+"PROPN", "w")
    }
    return files

def closeDictionaryFiles(dictionaries):

    for dict in dictionaries:
        dict.close()
 

def main(dictionnaryFilePath:str, languageCode:str):

    print("entering the main")
    nlp = spacy.load(spacyLibraryFromCode(languageCode))
    dictionaries = generateDictionaryFiles( "../dict_"+ languageCode)
    wordList = open(dictionnaryFilePath,'r')
    
    for word in wordList.readlines():
        
        token = nlp(word)
        wordType = dictionaries[token.pos_]
        dictionaries[str(token.pos_)].write(word+"\n")

    closeDictionaryFiles(dictionaries)
    


if __name__ == "__main__":

    print("main du parser")
    #main(sys.argv[1], sys.argv[2])