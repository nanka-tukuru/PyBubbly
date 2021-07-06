import unittest
from strategy_bubble import *

class TestBubbleSort(unittest.TestCase):
    """BubbleSortテスト
    """

    def test_case1(self):
        srclist = [10,9,8,7,6,5,4,3,2,1,0]
        anslist = [0,1,2,3,4,5,6,7,8,9,10]
        context = SortingContext(BubbleSort())
        context.sort(srclist)
        self.assertListEqual(srclist, anslist)
 
if __name__ == "__main__":
    unittest.main()
