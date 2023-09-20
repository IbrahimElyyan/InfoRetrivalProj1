import reader
import tokenizer
import lowercaser
import porter_stemmer
import stopword_remover

"""
STEP 1: read the Reuter’s collection and extract the raw text of each
Reuter’s news item (these are your documents) from the corpus
"""
# Path to the directory where the corpus is stored
reuters21578_path = r'C:\Users\ibrah\OneDrive\Desktop\reuters21578'


sample_documents = reader.read_reuters21578(reuters21578_path)
tokenized_sample_documents = tokenizer.tokenize_reuters21578(sample_documents)
