class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nge_map = {}
        stack = []
        
        for num in nums2:
            # Chota element milne par map me save karein
            while stack and stack[-1] < num:
                nge_map[stack.pop()] = num
            stack.append(num)
            
        # Bache huye elements ke liye -1
        while stack:
            nge_map[stack.pop()] = -1
            
        # nums1 ke liye answer nikalein
        return [nge_map[num] for num in nums1]
