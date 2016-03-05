import unittest
from PlayMap import *

testMap = PlayMap()

class TestPlayMap(unittest.TestCase):

    def testSetDiff(self):
        self.assertEqual(testMap.diff, 0)

        testMap.setDiff(1)
        self.assertEqual(testMap.diff, 1)

        testMap.setDiff(2)
        self.assertEqual(testMap.diff, 2)

    #def testUpdateState(self):
    
    #def testIsSnakeDead(self):

    def testDidSnakeHitBorder(self):
    	# test left
        testMap.snake.points[0].left = -1
        self.assertEqual(testMap.didSnakeHitBorder(), True)
        testMap.snake.points[0].left = 0
        self.assertEqual(testMap.didSnakeHitBorder(), False)
        testMap.snake.points[0].left = 1
        self.assertEqual(testMap.didSnakeHitBorder(), False)
        testMap.snake.points[0].left = testMap.width + 1
        self.assertEqual(testMap.didSnakeHitBorder(), True)
        testMap.snake.points[0].left = testMap.width
        self.assertEqual(testMap.didSnakeHitBorder(), True)
        testMap.snake.points[0].left = testMap.width - 1 
        self.assertEqual(testMap.didSnakeHitBorder(), False)

        # test top
        testMap.snake.points[0].top = 19 
        self.assertEqual(testMap.didSnakeHitBorder(), True)
        testMap.snake.points[0].top = 20
        self.assertEqual(testMap.didSnakeHitBorder(), False)
        testMap.snake.points[0].top = 21
        self.assertEqual(testMap.didSnakeHitBorder(), False)
        testMap.snake.points[0].top = testMap.height + 1
        self.assertEqual(testMap.didSnakeHitBorder(), True)
        testMap.snake.points[0].top = testMap.height
        self.assertEqual(testMap.didSnakeHitBorder(), True)
        testMap.snake.points[0].top = testMap.height - 1 
        self.assertEqual(testMap.didSnakeHitBorder(), False)

    def testDidSnakeSelf(self):
		# put snake back to starting pos
		testMap.snake = Snake(250, 290)

		# test alive
		self.assertEqual(testMap.didSnakeHitSelf(), False)

		# test power up
		testMap.snake.points[0] = testMap.snake.points[19]
		self.assertEqual(testMap.didSnakeHitSelf(), False)

		# test death
		testMap.snake.points[0] = testMap.snake.points[1]
		self.assertEqual(testMap.didSnakeHitSelf(), True)
	
    def testIsSnakeDead(self):
		# put snake back to starting pos
		testMap.snake = Snake(250, 290)

		self.assertEqual(testMap.isSnakeDead(), False)
		testMap.snake.points[0].left = -1
		self.assertEqual(testMap.isSnakeDead(), True)
		testMap.snake.points[0] = testMap.snake.points[1]
		self.assertEqual(testMap.isSnakeDead(), True)

    def testUpdateState(self):
		# put snake back to starting pos
		testMap.snake = Snake(250, 290)	
		testMap.food.position.left = 250
		testMap.food.position.top = 300
		# test move and eating food
		testMap.updateState()
		self.assertEqual(testMap.score, 21)

		# test move and not eating food
		testMap.updateState()
		self.assertNotEqual(testMap.score, 22)

    def testGetCurrentState(self):
    	# put snake back to starting pos
		testMap.snake = Snake(250, 290)

		testMap.snake.points[0] = testMap.snake.points[1]
		self.assertEqual(testMap.getCurrentState(), -1)

		# put snake back to starting pos
		testMap.snake = Snake(250, 290)
		testMap.powerUpStatus = True
		self.assertEqual(testMap.getCurrentState(), [testMap.snake.points, testMap.food.position, testMap.gameStatsBar, testMap.powerUpIndicator, testMap.powerUp.position])
		testMap.powerUpStatus = False
		self.assertEqual(testMap.getCurrentState(), [testMap.snake.points, testMap.food.position, testMap.gameStatsBar, -1, -1])



if __name__ == '__main__':
    unittest.main(verbosity = 2)