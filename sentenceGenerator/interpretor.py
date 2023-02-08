import spacy
import sys



def main(text:str, languageCode:str):
    nlp = spacy.load(languageCode + "_core_web_sm")

    tokens = tokens = nlp(text)
    for token in tokens:
        print(token, "-------->", token.lemma_ )
    


if __name__ == "__main__":

    main(sys.argv[1], sys.argv[2])