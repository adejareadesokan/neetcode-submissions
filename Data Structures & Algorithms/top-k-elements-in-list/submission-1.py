from collections import Counter
import heapq
class Solution:

    def topKFrequent(self, nums, k):
        freq = Counter(nums)                
        heap = []                          
        for num, count in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                if count > heap[0][0]:
                    heapq.heapreplace(heap, (count, num))
        return [num for _, num in heap]
        