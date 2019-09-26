import unittest
import kamer

class TestBasicClass(unittest.TestCase):

    def setUp(self):
        self.testKamer = kamer.Kamer("keuken")
        self.testKamer2 = kamer.Kamer("woonkamer")
        self.testSleutel = kamer.Key(1286)
        self.testDoor = kamer.Door(1)
    
        # self.testKamer = None

    def test_kamerBestaat(self):
        self.assertIsNotNone(self.testKamer)
        self.assertIsInstance(self.testKamer, kamer.Kamer)
    
    def test_kamerNaam(self):
        self.assertEqual(self.testKamer.naam,"keuken")

    def test_Door(self):
        self.assertEqual(self.testDoor.openDoor, 1)

    # def test_increment(self):
    #     self.func.increment_state()
    #     self.assertEqual(self.func.state, 1)

    # def test_clear_state(self):
    #     self.func.clear_state()
    #     self.assertEqual(self.func.state, 0)
        
if __name__ == '__main__':
    unittest.main()
    