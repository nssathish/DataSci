from typing import Counter

from nltk.tokenize import sent_tokenize

sentences = sent_tokenize(
    "The Nobel Prize is a set of five annual international awards bestowed in several categories by Swedish and Norwegian institutions in recognition of academic, cultural, or scientific advances. In the 19th century, the Nobel family who were known for their innovations to the oil industry in Azerbaijan was the leading representative of foreign capital in Baku. The Nobel Prize was funded by personal fortune of Alfred Nobel. The Board of the Nobel Foundation decided that after this addition, it would allow no further new prize.".lower()
)


def prob(word):
    total_sentences = len(sentences)
    sentences_containing_word = 0

    for sentence in sentences:
        occurrence = Counter(sentence.split())[word]
        sentences_containing_word += occurrence

    return sentences_containing_word / total_sentences


print(prob("nobel"))
print(prob("prize"))
