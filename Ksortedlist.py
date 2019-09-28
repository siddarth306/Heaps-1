# Time Complexity: O(nlog(k)) where n is the total number of elements
# Space Complexity: O(k) 
# Approach: Maintain a k pointer array having pointer to current node of each list. Maintain a min heap of all the pointed nodes.
#			Pop the min node from the heap and append it to the result list. Move the pointer of that list to the next node and add it to the min heap.
#			Finally print the result.
#
# Missed Cases: [], [[],[1]], [[]]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k_ptr = []
        k_heap = []
        result_head = None
        
        if not lists:
            return None
        idx = 0
        for i in lists:
            if i:
                k_ptr.append(i)
                heapq.heappush(k_heap, (i.val, idx, i))
                idx +=1
        
        while len(k_heap) != 0:
            elem, k_idx, k = heapq.heappop(k_heap)
            
            #print(elem, k_idx, k)
            if result_head is None:
                if k is not None:
                    result_head = result = k
                    k_ptr[k_idx] = k.next
                    k.next = None
            else:
                result.next = k
                k_ptr[k_idx] = k.next
                k.next = None
                result = result.next
                
            if k_ptr[k_idx] is not None:
                heapq.heappush(k_heap, (k_ptr[k_idx].val, k_idx, k_ptr[k_idx] ))
            
        return result_head
            