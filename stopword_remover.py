from nltk.corpus import stopwords


#STEP 5: given a list of stop words, remove those stop words from text.
def remove_stopwords(docs):
    stop_words = set(stopwords.words('english'))
    clear_docs = []
    for doc in docs:
        words = doc.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        clear_docs.append(' '.join(filtered_words))
    return clear_docs