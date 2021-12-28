import unittest
from RanPass import Password


class PassGenTest(unittest.TestCase):
    
    def setUp(self):
        self.sample = Password.Generator()
        self.validator = Password.Validator
        print('PassGenTest SetUp Run...')
        
    def test_Password(self):
        result = self.validator(self.sample)
        self.assertTrue(result)
        print('Test Password Run...')
        
    def tearDown(self):
        print('PassGenTest Teardown Run...')
        
class PassValTest(unittest.TestCase):
    
    def setUp(self):
        self.validator = Password.Validator
        print('PassValTest SetUp Run...')
        
    def test_len(self):
        sample = 'Testl!' #Password must be at least 8 characters
        result = self.validator(sample)
        self.assertFalse(result, False)
        print('Length Test Run...')

    def test_upperCase(self):
        sample = 'testupper_case!#'
        result = self.validator(sample)
        self.assertFalse(result, False)
        print('UpperCase Test Run...')

    def test_special_chars(self):
        sample = 'testspecialchars'
        result = self.validator(sample)
        self.assertFalse(result, False)
        print('Special Chars Test Run...')
                                
    def tearDown(self):
        print('PassValTest Teardown Run...')
        
        
if __name__ == '__main__':
    unittest.main()