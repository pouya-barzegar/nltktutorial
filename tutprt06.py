# Chinking - Removing things from a chunk you already set up.
# Achieves the same effect as Chunking but in th opposite way:
# In Chunking, first everything is separate,
# then they are grouped together specifically.
# In Chinking, first everything is grouped ,
# then they are split from the group specifically.
import nltk
from nltk.corpus import state_union
# PunktSentenceTokenizer is a ML tokenizer!
from nltk.tokenize import PunktSentenceTokenizer


def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            '''Here begins the Chunking with a chick'''
            chuckGram = r"""Chuck: {<.*>+}
                                   }<VB.?|IN|DT|TO>+{"""

            chuckParser = nltk.RegexpParser(chuckGram)
            chunked = chuckParser.parse(tagged)

            chunked.draw()
            # print(chunked)

    except Exception as e:
        print(str(e))


# get text
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

# apply train text
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# apply tokenizer on text
tokenized = custom_sent_tokenizer.tokenize(sample_text)

# call function to tokenize and chunk
process_content()
