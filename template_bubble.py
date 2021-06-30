from abc import ABCMeta, abstractmethod

class TemplateBubble(metaclass=ABCMeta):
    """Template Methodパターンを使ったバブルソート
    """

    def __init__(self, srclist):
        # 参照渡しなので、パラメータのリストが更新される
        self._list = srclist

    @abstractmethod
    def compare(self, a, b):
        pass

    def sort(self):
        """以下を参考にしました
        <https://watlab-blog.com/2020/08/12/bubble-sort/>
        """
        data = self._list
        n = len(data)
        for i in range(n):                                      # i=0からnまでのループ
            for j in range(n-1, i, -1):                         # n-1からiまでの逆ループ
                if self.compare(data[j-1], data[j]) > 0:        # 隣り合う値を比較
                    data[j], data[j-1] = data[j-1], data[j]     # 交換

class NumBubble(TemplateBubble):
    """数値のバブルソート
    """
    def compare(self, a, b):
        if a > b:
            return 1
        else:
            return 0
