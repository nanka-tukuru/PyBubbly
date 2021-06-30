import unittest
from template_bubble import NumBubble

class TestIntBubble(unittest.TestCase):
    """NumBubbleテスト
    """

    def test_case1(self):
        srclist = [10,9,8,7,6,5,4,3,2,1,0]
        anslist = [0,1,2,3,4,5,6,7,8,9,10]
        numBubble = NumBubble(srclist)
        numBubble.sort()
        self.assertListEqual(srclist, anslist)
 
if __name__ == "__main__":
    unittest.main()
