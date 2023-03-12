import spacy
import sys


def spacyLibraryFromCode(languageCode:str):

    switch = {
        "fr":"fr_core_news_sm",
        "en":"en_core_web_sm"
    }
    return switch.get(languageCode)

def main(text:str, languageCode:str):
    nlp = spacy.load(spacyLibraryFromCode(languageCode))

    tokens = nlp(text)
    for token in tokens:
        print(token, "-------->", token.lemma_, token.pos_ )
    


if __name__ == "__main__":

    main(sys.argv[1], sys.argv[2])