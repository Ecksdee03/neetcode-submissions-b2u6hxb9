import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums
        heapq.heapify(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h,val)
        return heapq.nlargest(self.k, self.h)[-1]
