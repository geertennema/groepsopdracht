import unittest


from voorwerpen import Voorwerp, Key

class voorwerpenTest(unittest.TestCase):

   def test_name(self):
       voorwerp = Voorwerp("player") #omdat het een test is tussen aanhalingstekens
       self.assertEqual(voorwerp.name, "player")


if __name__ == '__main__':
    unittest.main()    

