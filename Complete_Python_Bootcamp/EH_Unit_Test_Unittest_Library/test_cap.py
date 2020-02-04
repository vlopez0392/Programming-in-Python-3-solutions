### SECTION 10 - Errors and Exceptions Handling

### When writing test functions, its convenient to write simple functions first.
import unittest
import Cap

##General structure of a test
class TestCap(unittest.TestCase): ##Create a class and inherit from unittest.TestCase

    def test_one_word(self):      ##Define the methods to test your script
        text = 'python'
        result = Cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monthy python'
        result = Cap.cap_text(text)
        self.assertEqual(result, 'Monthy Python')

if __name__ == '__main__':
    unittest.main()