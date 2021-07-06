import nltk
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
import re
import string

def detect(test):
    question_word_list = ['what',     'where','when','how','why','did','do','does','have','has','am','is','are','can','could','may','would','will','should'
        "didn't","doesn't","haven't","isn't","aren't","can't","couldn't","wouldn't","won't","shouldn't"]
    punc = "["+string.punctuation+"]"
    sentences = re.split(punc.replace('?', ''), test)
    question = False
    for s in sentences:
        s=s.strip()
        if len(s) > 1:
            if '?' in s:
                question = True
                break
            else:
                words = word_tokenize(s.lower())
#                 print(words[0])
                if words[0] in question_word_list:
                    question = True
                    break
    if question:
        return 1
    else:
        return 0
    
    