import os
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

"""
STEP 1: read the Reuter’s collection and extract the raw text of each
Reuter’s news item (these are your documents) from the corpus
"""
# Path to the directory where the corpus is stored
corpus_path = r'C:\Users\ibrah\OneDrive\Desktop\reuters21578'

def read_reuters_documents(corpus_path):
    documents = []
    for filename in os.listdir(corpus_path):
        if filename.startswith('reut'):
            with open(os.path.join(corpus_path, filename), 'r') as file:
                documents.append(file.read())
    return documents

#STEP 2: tokenize function
def tokenize_documents(documents):
    tokenized_documents = [word_tokenize(doc) for doc in documents]
    return tokenized_documents

#STEP 3: lowercasing
def lowercase_documents(documents):
    lowercased_documents = [doc.lower() for doc in documents]
    return lowercased_documents

#STEP 4: apply Porter stemmer
def apply_porter_stemmer(documents):
    porter = PorterStemmer()
    stemmed_documents = [' '.join([porter.stem(word) for word in doc.split()]) for doc in documents]
    return stemmed_documents

"""
STEP 5: given a list of stop words, remove those stop words from text. 
Note that your code has to accept the stop word list as a parameter,
do not hardcode a particular list
"""
def remove_stopwords(documents):
    stop_words = set(stopwords.words('english'))
    cleaned_documents = []
    for doc in documents:
        words = doc.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        cleaned_documents.append(' '.join(filtered_words))
    return cleaned_documents
print("New")
sample_documents = read_reuters_documents(corpus_path)
tokenized_sample_documents = tokenize_documents(sample_documents)
