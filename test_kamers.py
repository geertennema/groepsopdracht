import unittest
from Kamers import Kamer 

class KamerTest(unittest.TestCase):

    def setUp(self):
        self.kamer1 = Kamer(
            open = 1,
            close = 0,
            key = 'key'
        )
        