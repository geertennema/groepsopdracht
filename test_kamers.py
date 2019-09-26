import unittest
from kamerdef import Kamer 

class KamerTest(unittest.TestCase):

    def setUp(self):
        self.kamer1 = Kamer(
            open = 1,
            close = 0,
            key = 'key'
        )

if __name__ == '__main__':
    unittest.main()
        