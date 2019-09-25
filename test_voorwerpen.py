import unittest


from voorwerpen import Voorwerp

class voorwerpenTest(unittest.TestCase):

   def test_name(self):
       voorwerp = Voorwerp("speler") #omdat het een test is
       self.assertEqual(voorwerp.naam, "speler")


if __name__ == '__main__':
    unittest.main()
