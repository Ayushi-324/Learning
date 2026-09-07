import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        res = []
        if not nums1 or not nums2: return res
        
        min_heap = []
        for i in range(min(len(nums1), k)): #nitial push: (sum, idx_in_nums1, idx_in_nums2)
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
            
        while min_heap and len(res) < k: # Pop K times to get smallest pairs
            _, i, j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])
            
            if j + 1 < len(nums2):  # Next elem from nums2 for the same nums1[i]
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return res
