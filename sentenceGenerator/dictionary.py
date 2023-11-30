import os
import shutil
from typing import Dict


class Word:
    def __init__(self, word: str, stem:str = None, position:str = None, language:str = None) -> None:
        self.word = word
        self.stem = stem
        self.position = position
        self.language = language

    def word(self):
        return self.word
    
    def stem(self):
        return self.stem
    
    def position(self):
        return self.position
    
    def language(self):
        return self.language

# class Position:
#     def __init__(self, positionName: str):
#         self.name = positionName
#         self.stems = {}
    
#     def addWord(self, word: Word):
#         if word.stem not in self.stems:
#             self.stems[word.stem] = Stem(word.stem)
#         self.stems[word.stem]


# class Stem:
#     def __init__(self, stemWord: str):
#         self.stemWord = stemWord
#         self.words = []
    
#     def addWord(self, word:Word):
#         self.words.append(word)
    
#     def words(self):
#         return self.words
        

class Dictionary:

    def __init__(self, name:str, languageCode: str, dictionaryFolderPath: str) -> None:
        self.name = name
        self.languageCode = languageCode
        self.dictionaryFolderPath = dictionaryFolderPath + languageCode + "/"
        print(self.dictionaryFolderPath)
        self.dictionary = []

    def loadDictionary(self):
        #If too slow to start, get words on the go
        if not os.path.exists(self.dictionaryFolderPath): return None
        positions = os.listdir(self.dictionaryFolderPath)
        for position in positions:
            positionPath = self.dictionaryFolderPath + position + "/"
            stemFiles = os.listdir(positionPath)
            for stemFile in stemFiles:
                filePath = positionPath + stemFile
                stem, fileExtention = os.path.splitext(stemFile)
                with open(filePath, 'r') as file:
                    words = file.read().split('\n')
                    for word in words:
                        self.addWord(word, stem, position)
                
    
    def save(self):
        self.clear()
        for word in self.dictionary:

            wordPath = self.dictionaryFolderPath + word["position"] + "/"
            os.makedirs(wordPath, exist_ok=True)
            wordPath = wordPath + word["stem"] + ".txt"
            fileWriteMode = 'a' if os.path.isfile(wordPath) else 'w'
            with open(wordPath, fileWriteMode) as stemFile:
                textToWrite = "\n" + word["word"]  if (fileWriteMode == 'a') else word["word"]
                stemFile.write(textToWrite)

    

    def clear(self):

        if not os.path.exists(self.dictionaryFolderPath): return None

        files = os.listdir(self.dictionaryFolderPath)
        for fileName in files: 
            
            filePath = self.dictionaryFolderPath + fileName
            if os.path.isdir(filePath): shutil.rmtree(filePath)
                
            else: os.remove(filePath)

    def addWord(self, word:str, stem:str, position:str):
        self.dictionary.append({"word": word, "stem": stem, "position": position})

    def getWordsFromStem(self, stemToFind:str, position:str):
        #Get the words from the file
        stemFile = self.dictionaryFolderPath + position + "/" + stemToFind + ".txt"
        wordsWithStem = []
        if os.path.exists(stemFile):
            with open(stemFile, 'r') as file:
                words = file.read().split('\n')
                for word in words:
                    wordsWithStem.append({"word": word, "stem": stemToFind, "position": position})
        return wordsWithStem


        #When it is loaded in memory
        # wordsWithStem = []
        # for word in self.dictionary:
        #     if(word["stem"] == stemToFind and word["position"] == position):
        #         wordsWithStem.append(word)
        # return wordsWithStem
       
