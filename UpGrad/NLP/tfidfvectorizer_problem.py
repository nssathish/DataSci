import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer

# Initialize the Porter Stemmer
stemmer = PorterStemmer()

# Define the documents
documents = [
    "The coach lumbered on again, with heavier wreaths of mist closing round it as it began the descent.",
    "The guard soon replaced his blunderbuss in his arm-chest, and, having looked to the rest of its contents, and having looked to the supplementary pistols that he wore in his belt, looked to a smaller chest beneath his seat, in which there were a few smith's tools, a couple of torches, and a tinder-box.",
    "For he was furnished with that completeness that if the coach-lamps had been blown and stormed out, which did occasionally happen, he had only to shut himself up inside, keep the flint and steel sparks well off the straw, and get a light with tolerable safety and ease (if he were lucky) in five minutes.",
    "Jerry, left alone in the mist and darkness, dismounted meanwhile, not only to ease his spent horse, but to wipe the mud from his face, and shake the wet out of his hat-brim, which might be capable of holding about half a gallon.",
    "After standing with the bridle over his heavily-splashed arm, until the wheels of the mail were no longer within hearing and the night was quite still again, he turned to walk down the hill.",
]

# Preprocess the documents
processed_docs = []
for doc in documents:
    tokens = word_tokenize(doc)
    stemmed_tokens = [
        stemmer.stem(token)
        for token in tokens
        if token not in stopwords.words("english")
    ]  # remove stopwords
    processed_docs.append(" ".join(stemmed_tokens))

# Initialize the TfidfVectorizer
vectorizer = TfidfVectorizer()  # Initialize

# Fit and transform the vectorizer on processed documents
tfidf_matrix = vectorizer.fit_transform(processed_docs)  # Create TF IDF matrix

# Get the index of 'belt' in feature names
index = vectorizer.get_feature_names_out()
print(index)

# Print the tf-idf score of 'belt' in the second document
# print the score of belt present in document 2 at index == index in the tfidf_matrix array
print("""Print the score rounded to 2 digits""")

# # To verify if the score is correct, you can
# # convert the TF-IDF matrix to a DataFrame

df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())

# # And, display the column for 'belt'

print(round(sum(df["belt"]), 2))
