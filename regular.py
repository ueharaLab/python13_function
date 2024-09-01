import unicodedata
import re

def normalize_jpn(text):
    
    normalized = unicodedata.normalize('NFKC', text)
    normalized = normalized.lower()
    char = re.findall('[a-zA-Z一-龥ぁ-んァ-ンー々。、]+', normalized)
    sentence =''.join(char)
    return sentence