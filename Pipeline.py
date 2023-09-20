import reader
import tokenizer
import lowercaser
import porter_stemmer
import stopword_remover

# Path to the directory where the corpus is stored
reuters21578_path = r'C:\Users\ibrah\OneDrive\Desktop\reuters21578'

documents = reader.read_reuters21578(reuters21578_path)[:5]
tokenized_documents = tokenizer.tokenize_reuters21578(documents)
lowercased_documents = lowercaser.lowercase_reuters21578(documents)
stemmed_documents = porter_stemmer.porter_stem_reuters21578(documents)
stopword_free_documents = stopword_remover.remove_stopwords(documents)

# Writing the reader output files
for i in range(5):
    with open(f'Reader-output{i + 1}.txt', 'w') as file:
        file.write(documents[i])

# Writing the tokenized output files
for i in range(5):
    with open(f'Tokenizer-output{i + 1}.txt', 'w') as file:
        file.write('\n'.join(tokenized_documents[i]))


# Writing lowercased output files
for i in range(5):
    with open(f'Lowercased-output{i + 1}.txt', 'w') as file:
        file.write(lowercased_documents[i])
        
# Writing stemmed output files
for i in range(5):
    with open(f'Stemmed-output{i + 1}.txt', 'w') as file:
        file.write(stemmed_documents[i])

# Writing stopwprd removed output files
for i in range(5):
    with open(f'No-stopword-output{i + 1}.txt', 'w') as file:
        file.write(stopword_free_documents[i])

