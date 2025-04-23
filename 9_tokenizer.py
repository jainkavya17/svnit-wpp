import string
import re
def tokenize(s):
    pattern={'url': r'\w+\.com',
            'email': r'[\w\.-]+@[\w\.-]+\.\w+',
            'date': r'\b(?:\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{4}[-/.]\d{1,2}[-/.]\d{1,2})\b',
            'number': r'\b\d{1,3}(?:,\d{2,3})*(?:\.\d+)?\b|\b\d+/\d+\b',
            'social_handle': r'@[A-Za-z0-9_]+',
            'punctuation': r'[""“”‘’!()\-\[\]{};:\'\,<>./?@#$%^&*_~]',
            'hindi_word': r'[\u0900-\u097F]+'
            }
    for key in pattern:
        print(key)
        matches=re.findall(pattern[key],s)
        token=[x for x in matches]
        print(token)
tokenize("test@gmail.com 12-12-12 33.14 ,@jainkavya, www.google.com ")

