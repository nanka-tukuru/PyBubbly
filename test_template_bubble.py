import unittest
from template_bubble import NumBubble

class TestIntBubble(unittest.TestCase):
    """NumBubbleテスト
    """

    def test_case1(self):
        src_list = [10,9,8,7,6,5,4,3,2,1,0]
        ans_list = [0,1,2,3,4,5,6,7,8,9,10]
        numBubble = NumBubble()
        numBubble.list = src_list
        numBubble.bubble_sort()
        self.assertListEqual(numBubble.list, ans_list)
 
if __name__ == "__main__":
    unittest.main()
