
import unittest
from calcula_media import calcula_media

class TestCalculaMedia(unittest.TestCase):
    
    def test_media_basica(self):
        self.assertEqual(calcula_media(10, 5, 7), 7.33)

    def test_media_zeros(self):
        self.assertEqual(calcula_media(0, 0, 0), 0)

    def test_media_maximos(self):
        self.assertEqual(calcula_media(10, 10, 10), 10)

    def test_media_decimais(self):
        self.assertAlmostEqual(calcula_media(5.5, 7.3, 8.2), 7.0, places=1)

if __name__ == '__main__':
    unittest.main()
