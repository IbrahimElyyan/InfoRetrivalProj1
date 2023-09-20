import os


"""
STEP 1: read the Reuter’s collection and extract the raw text of each
Reuter’s news item (these are your documents) from the corpus
"""
def read_reuters21578(corpus):
    documents = []
    for filename in os.listdir(corpus):
        if filename.startswith('reut'):
            with open(os.path.join(corpus, filename), 'r') as file:
                documents.append(file.read())
    return documents