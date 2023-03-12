import sys

def main(languageCode:str):

    print(languageCode + " dictionnary")


if __name__ == "__main__":

    DICTIONNARIES_FOLDER_PATH = "./Dictionnaries/"
    args = sys.argv[1:]
    main(sys.argv[1])