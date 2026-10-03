documents = [
    "there was a place on my ankle that was itching",
    "but I did not scratch it",
    "and then my ear began to itch",
    "and next my back",
]

from nltk.tokenize import word_tokenize

words = set()
for document in documents:
    document_words = word_tokenize(document)
    # no_stops = [
    #     word for word in document_words if word not in stopwords.words("english")
    # ]
    [words.add(word) for word in document_words]

print(words)
print(len(words))

from nltk.corpus import stopwords


def preprocess(document):
    "changes document to lower case and removes stopwords"

    # change sentence to lower case
    document = document.lower()

    # tokenize into words
    words = word_tokenize(document)
    # words = document.split()

    # remove stop words
    words = [word for word in words if word not in stopwords.words("english")]

    # join words to make sentence
    document = " ".join(words)

    return document


print(
    preprocess(
        "Vapour, Bangalore has a really great terrace seating and an awesome view of the Bangalore skyline"
    )
)
print(
    preprocess(
        "The beer at Vapour, Bangalore was amazing. My favourites are the wheat beer and the ale beer."
    )
)
print(preprocess("Vapour, Bangalore has the best view in Bangalore."))
