import unittest
from src.utils.sanitizer import Sanitizer

class TestSanitizer(unittest.TestCase):
    def setUp(self) -> None:
        self.sanitizer = Sanitizer()
        return super().setUp()

    def test_should_sanitize_link_without_query(self):
        expect = 'https://www.immoweb.be/fr/annonce/maison/a-vendre/gembloux/5030/8726798'
        operand = 'https://www.immoweb.be/fr/annonce/maison/a-vendre/gembloux/5030/8726798'
        self.assertEqual(expect, self.sanitizer.sanitizeLink(operand))
    
    def test_should_sanitize_and_delete_query(self):
        expect = 'https://www.immoweb.be/fr/annonce/maison/a-vendre/gembloux/5030/8726798'
        operand = 'https://www.immoweb.be/fr/annonce/maison/a-vendre/gembloux/5030/8726798?toto=2'
        self.assertEqual(expect, self.sanitizer.sanitizeLink(operand))

if __name__ == '__main__':
    unittest.main()
