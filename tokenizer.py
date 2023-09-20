from nltk.tokenize import word_tokenize


#STEP 2: tokenize function
def tokenize_reuters21578(docs):
    tokenized_docs = [word_tokenize(doc) for doc in docs]
    return tokenized_docs