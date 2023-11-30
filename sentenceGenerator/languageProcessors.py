import nltk
import spacy
from nltk.stem import WordNetLemmatizer
from dictionary import Word



class ILanguageProcessor(object):
    def __init__(self):
        pass

    def tokenise(self, words:str):
        raise Exception("No implementation")


class SpacyProcessor(ILanguageProcessor):

    def spacyLibraryFromCode(self, languageCode:str):

        switch = {
            "fr":"fr_core_news_sm",
            "en":"en_core_web_sm"
        }
        return switch.get(languageCode)

    def __init__(self, languageCode: str):
        
        self.stemmer = spacy.load(self.spacyLibraryFromCode(languageCode))

    def tokenise(self, words: str) -> list[Word]:
        tokens = self.stemmer(words)
        tokenisedWords = []

        for token in tokens:
            tokenisedWords.append(Word(token, token.lemma_, token.pos_))
        
        return tokenisedWords


