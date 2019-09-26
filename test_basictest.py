import unittest
from kamerdef import Kamer

class TestBasicClass(unittest.TestCase):

    def setUp(self):
        self.testKamer = Kamer("keuken", "deur1")

    def test_kamerBestaat(self):
        self.assertIsNotNone(self.testKamer)
        self.assertIsInstance(self.testKamer, Kamer)
    
    def test_kamerNaam(self):
        self.assertEqual(self.testKamer.name,"keuken")

    # def test_increment(self):
    #     self.func.increment_state()
    #     self.assertEqual(self.func.state, 1)

    # def test_clear_state(self):
    #     self.func.clear_state()
    #     self.assertEqual(self.func.state, 0)
        
if __name__ == '__main__':
    unittest.main()
    