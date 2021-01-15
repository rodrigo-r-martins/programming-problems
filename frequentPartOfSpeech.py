'''
- Most common part of speech using NLTK

Given the following text, can you find the most frequent part of speech (POS) used in the text below? 

To solve this question, we recommend you start with Natural Language Toolkit (NLTK). Within NLTK you will want to look into the pos_tag() function. 
NLTK is a great tool that allows us to easily analyze text. There are a lot of interesting applications for NLTK, including sentiment analysis (can be applied to social media feeds / classifying reviews for a product) and spam filters (identifying text as spam or !spam).
'''

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
from nltk.probability import FreqDist

#text from Harper Lee, To Kill a Mockingbird
text = '''
Atticus said to Jem one day, “I’d rather you shot at tin cans in the backyard, but I know you’ll go after birds. 
Shoot all the blue jays you want, if you can hit ‘em, but remember it’s a sin to kill a mockingbird.” 
That was the only time I ever heard Atticus say it was a sin to do something, and I asked Miss Maudie about it. 
“Your father’s right,” she said. 
“Mockingbirds don’t do one thing except make music for us to enjoy. 
They don’t eat up people’s gardens, don’t nest in corn cribs, they don’t do one thing but sing their hearts out for us. 
That’s why it’s a sin to kill a mockingbird.
'''

text_tags = nltk.pos_tag(word_tokenize(text))
print(text_tags)
frequent = FreqDist(tag for (word, tag) in text_tags)

import collections
word_counts = collections.Counter((words[0] for words in text_tags 
                                    if len(words[0])>1))   # just words, not marks

print('============================================================================================')
print(f'The five most frequent words are: {word_counts.most_common(5)}')    # Five more frequent
print('============================================================================================')

