from .dictionaries import RUSSIAN_DICT , ARABIC_DICT , INDIE_DICT , CHINE_DICT
import langid


dictionary = {
    'hi' : INDIE_DICT, 
    'ar' : ARABIC_DICT ,
    # fa = Persian language because there is words in arabic detect as persian
    'fa' : ARABIC_DICT ,
    'ru' : RUSSIAN_DICT ,
    'zh' : CHINE_DICT
}

# function to translate the letters 

def detector_lang(word):
    print(f'word : {word}')
    txt=str(word)
    # ***** this line to detect language
    detector = langid.classify(txt)
    print(f'detector : {detector}')
    # ***** convert the set result to list to get the first value
    language = list(detector)[0]

    return language


# **** translate function
def translate_letters(word):
    
    # get the result of detector_lang ==> function
    language = detector_lang(word)
    # get the dictionary of the detector language
    get_language = dictionary[language]

    word = word.upper()

    char=''

    for i in word:

        if i in get_language.keys():

            char += get_language[i]
            char = char.strip()
            char = char.lower()
        
    return char
    


