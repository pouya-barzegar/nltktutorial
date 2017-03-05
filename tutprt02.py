# Removing stopwords takes out all the fluff words of English
# in order to keep what's important.

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

example_sentence = "Hello class, this is first step in stripping down sentences\
                    to get the important words."

stop_words = set(stopwords.words("english"))
# print(stop_words)

words = word_tokenize(example_sentence)

filtered_sentence = [i for i in words if i not in stop_words]

print(filtered_sentence)
