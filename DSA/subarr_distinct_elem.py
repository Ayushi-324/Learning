class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)

        for i in range(n):  #outer loop subarr start 
            distinct_elem = set()  #har br naya khali set 

            for j in range(i, n):  #inner loop subarr end 
                distinct_elem.add(nums[j]) # set removes dumplicate 

                count = len(distinct_elem)  #take unique elem count - do square add in sum  
                total_sum += count * count

        return total_sum

# time - O(n2) nested loop   space = O(n) set uniq elem store 
