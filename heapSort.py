import math

class HeapSort:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self.arr = [1,2,3]
        return self.arr
sl = HeapSort([1,2,3])

print(sl.sort())
