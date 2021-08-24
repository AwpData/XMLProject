import re
import string
from collections import Counter

import nltk
from lxml import etree
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords

nltk.download("stopwords")
nltk.download("wordnet")

stopwords_ = stopwords.words("english")
punctuation = list(string.punctuation)
lemma = WordNetLemmatizer()
root = etree.parse("news.xml").getroot()[0]
for i in root:
    title = i[0].text
    story = i[1].text
    word_tokenizer = nltk.word_tokenize(story.lower())
    word_tokenizer.sort(reverse=True)
    word_tokenizer = [lemma.lemmatize(word) for word in word_tokenizer]
    word_tokenizer = [word for word in word_tokenizer if word not in punctuation]
    word_tokenizer = [word for word in word_tokenizer if word not in stopwords_]
    word_tokenizer = [word for word in word_tokenizer if re.match(r"'[\w\d]+", word) is None]  # Make sure to de comment
    common_word_dict = Counter(word_tokenizer)
    print(title + ":")
    for word in common_word_dict.most_common(5):
        print(word[0], end=" ")
    print("\n")
