#STEP 3: lowercasing
def lowercase_reuters21578(docs):
    lowercase_docs = [doc.lower() for doc in docs]
    return lowercase_docs