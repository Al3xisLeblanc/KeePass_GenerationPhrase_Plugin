import spacy
import sys
from dictionary import Dictionary


def spacyLibraryFromCode(languageCode:str):

    switch = {
        "fr":"fr_core_news_sm",
        "en":"en_core_web_sm"
    }
    return switch.get(languageCode)

def main():
    # nlp = spacy.load(spacyLibraryFromCode(languageCode))

    # tokens = nlp(text)
    # for token in tokens:
    #     print(token, "-------->", token.lemma_, token.pos_ )
    
    dictionary = Dictionary("fr", "fr", DICTIONNARIES_FOLDER)

    while(True):
        word = input("Words to find: ")
        stemWords = dictionary.getWordsFromStem(word, "NOUN")
        print(stemWords)
    


if __name__ == "__main__":
    DICTIONNARIES_FOLDER = "./Dictionnaries/"
    main()