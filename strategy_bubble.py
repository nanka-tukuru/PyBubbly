from abc import ABCMeta, abstractmethod

class StrategySort(metaclass=ABCMeta):
    @abstractmethod
    def sort(self, srclist):
        pass

class BubbleSort(StrategySort):
    def compare(self, a, b):
        if a > b:
            return 1
        else:
            return 0

    def sort(self, srclist):
        """以下を参考にしました
        <https://watlab-blog.com/2020/08/12/bubble-sort/>
        """
        data = srclist
        n = len(data)
        for i in range(n):                                      # i=0からnまでのループ
            for j in range(n-1, i, -1):                         # n-1からiまでの逆ループ
                if self.compare(data[j-1], data[j]) > 0:        # 隣り合う値を比較
                    data[j], data[j-1] = data[j-1], data[j]     # 交換

class SortingContext:
    def __init__(self, strategySort):
        self._strategySort = strategySort

    def sort(self, srclist):
        self._strategySort.sort(srclist)
