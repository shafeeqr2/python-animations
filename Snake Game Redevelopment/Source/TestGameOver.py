import unittest
from GameOver import *

testGameOver = GameOver(20)

class TestGameOver(unittest.TestCase):

	def testUpdateState(self):
		testGameOver.updateState(21)
		self.assertEqual(testGameOver.score, 21)

	def testGetCurrentState(self):
		self.assertEqual(testGameOver.getCurrentState(),[testGameOver.score, testGameOver.retryButton, testGameOver.exitButton])

if __name__ == '__main__':
	unittest.main(verbosity = 2)