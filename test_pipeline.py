import os
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
        testing_sample = ["This text will be tokenized.", "Hope this works:)"]
        tokenized_sample = tokenizer.tokenize_reuters21578(testing_sample)
        self.assertEqual(len(tokenized_sample), len(testing_sample))
        expected_answer1 = ['This', 'text', 'will', 'be', 'tokenized', '.']
        self.assertEqual(tokenized_sample[0], expected_answer1)
        expected_answer2 = ['Hope', 'this', 'works', ':', ')']
        self.assertEqual(tokenized_sample[1], expected_answer2)

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
        # Add test cases for stopword removal
        # Ensure the output without stopwords matches the expected documents
        pass

if __name__ == '__main__':
    unittest.main()
