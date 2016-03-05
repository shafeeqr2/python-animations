import unittest
from GamePause import *

testGamePause = GamePause(20)

class TestGamePause(unittest.TestCase):

	def testUpdateState(self):
		testGamePause.updateState(21)
		self.assertEqual(testGamePause.score, 21)

	def testGetCurrentState(self):
		self.assertEqual(testGamePause.getCurrentState(),[testGamePause.score, testGamePause.resumeButton, testGamePause.menuButton, testGamePause.exitButton])

if __name__ == '__main__':
	unittest.main(verbosity = 2)