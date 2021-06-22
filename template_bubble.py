from abc import ABCMeta, abstractmethod

class Bubble(metaclass=ABCMeta):
    """Template Methodパターンを使ったバブルソート
    """

    @abstractmethod
    def get_list(self):
        pass

    @abstractmethod
    def compare(self, a, b):
        pass

    def bubble_sort(self):
        """以下を参考にしました
        <https://watlab-blog.com/2020/08/12/bubble-sort/>
        """
        data = self.get_list()
        n = len(data)
        for i in range(n):                                      # i=0からnまでのループ
            for j in range(n-1, i, -1):                         # n-1からiまでの逆ループ
                if self.compare(data[j-1], data[j]) > 0:        # 隣り合う値を比較
                    data[j], data[j-1] = data[j-1], data[j]     # 交換

class NumBubble(Bubble):
    def __init__(self):
        #TODO listはここじゃない
        self.list = []

    def get_list(self):
        #TODO listはここじゃない
        return self.list

    def compare(self, a, b):
        if a > b:
            return 1
        else:
            return 0
