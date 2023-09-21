import os
from nltk.corpus import stopwords
import unittest
import reader, tokenizer, lowercaser, porter_stemmer, stopword_remover

class TestReutersProcessing(unittest.TestCase):

    def test_read_reuters21578(self):
        test_path = 'test_text/'
        os.makedirs(test_path)
        with open(os.path.join(test_path, 'reut_test_reader.txt'), 'w') as f:
            f.write('This is a sample text to test reader function.')
            
        documents = reader.read_reuters21578(test_path)
        self.assertEqual(len(documents), 1)
        self.assertEqual(documents[0], 'This is a sample text to test reader function.')
        # Clean so no need to keep deleting the test_text file everytime you test
        os.remove(os.path.join(test_path, 'reut_test_reader.txt'))
        os.rmdir(test_path)
        
        
    def test_tokenize_reuters21578(self):
        testing_sample = ["This text will be tokenized."]
        tokenized_sample = tokenizer.tokenize_reuters21578(testing_sample)

        # Check the length of tokenized_sample
        self.assertEqual(len(tokenized_sample), len(testing_sample))

        # Check the tokenization of the first document
        expected_answer1 = 'This text will be tokenized .'
        self.assertEqual(tokenized_sample[0], expected_answer1)



    def test_lowercase_reuters21578(self):
        testing_sample = ["This text will be LOWERCASED."]
        lowercased_sample = lowercaser.lowercase_reuters21578(testing_sample)
        self.assertEqual(len(lowercased_sample), len(testing_sample))
        expected_answer = ["this text will be lowercased."]
        self.assertEqual(lowercased_sample, expected_answer)

    def porter_stem_reuters21578(self):
        test_sample = {
            'running': 'run',
            'calmly': 'calmli',
            'bats': 'bat',
            'walks': 'walk',
            'aptly': 'aptli'
        }
        for sample, expected_answer in test_sample.items():
            stemmed_word = porter_stemmer.porter_stem_reuters21578([sample])[0]
            self.assertEqual(stemmed_word, expected_answer)
    

    def test_remove_stopwords(self):
        stop_words = set(stopwords.words('english'))

        test_sample = {
            'This is a sample.': 'sample.',
            'The slow white bear': 'slow white bear',
            'I have a dog': 'dog'
        }

        for sample, expected_answer in test_sample.items():
            cleaned_text = stopword_remover.remove_stopwords([sample])
            self.assertEqual(cleaned_text, [expected_answer])

    def test_transitivity(self):
        reuters21578_path = r'your path to\reuters21578'
        documents = reader.read_reuters21578(reuters21578_path)[:5]
        tokenized_documents = tokenizer.tokenize_reuters21578(documents)
        lowercased_documents = lowercaser.lowercase_reuters21578(tokenized_documents)
        stemmed_documents = porter_stemmer.porter_stem_reuters21578(lowercased_documents)
        stopword_free_documents = stopword_remover.remove_stopwords(stemmed_documents)
        
if __name__ == '__main__':
    unittest.main()
