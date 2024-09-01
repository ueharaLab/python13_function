from janome.tokenizer import Tokenizer


def get_token(sentence, hinsi):
    t = Tokenizer()
    words=[]
    for token in t.tokenize(sentence):
    	hinshi = token.part_of_speech.split(',')
    	if hinshi[0] == hinsi :
            words.append(token.surface)
    return words
