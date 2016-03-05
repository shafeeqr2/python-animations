import pygame
import unittest
import copy
from MainMenu import *

class TestMainMenuPy(unittest.TestCase) :

    def setUp(self) :
        global mConstructor
        global stateChanges
        mConstructor = MainMenu()
        stateChanges = ['menu','game','gameOver','gamePause','fakeMenu']

        pass

    def test_constructor(self) :
        testObj = MainMenu()
        self.assertEquals(str(mConstructor),str(testObj))
        testObj.changeState('gameOver')
        self.assertNotEquals(str(mConstructor),str(testObj))

    def test_changeState(self) :
        for i in range(len(stateChanges)) :
            testObj = MainMenu()
            prevState = testObj.state
            testObj.changeState(stateChanges[i])
            if i>3 : self.assertEquals(testObj.state,prevState) 
            else : self.assertEquals(testObj.state, stateChanges[i])
            

if __name__ == '__main__' :
    unittest.main(verbosity=2)

