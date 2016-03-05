import unittest
from Food import *

foodA = Food()
foodB = Food()
foodC = Food()
foodD = Food()

class TestFood(unittest.TestCase):

  def testRandomPos(self):
      self.assertNotEqual(foodA.position, foodB.position)
      self.assertNotEqual(foodB.position, foodC.position)
      self.assertNotEqual(foodC.position, foodD.position)

if __name__ == '__main__':
    unittest.main(verbosity = 2)