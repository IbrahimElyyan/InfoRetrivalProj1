from nltk.stem import PorterStemmer


#STEP 4: apply Porter stemmer
def porter_stem_reuters21578(docs):
    porter = PorterStemmer()
    stemmed_docs = [' '.join([porter.stem(word) for word in doc.split()]) for doc in docs]
    return stemmed_docs