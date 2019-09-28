# Time Complexity: O(nlogk)
# Space Cimplexity: O(k
# Approach: Always maintain a min heap of the max k elements while iterating the array
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums[:k]:
            heapq.heappush(heap, i)
        for i in nums[k:]:
            x = heapq.heappop(heap)
            if x < i:
                heapq.heappush(heap, i)
            else:
                heapq.heappush(heap, x)
            #print(heap)
        
        return heapq.heappop(heap)