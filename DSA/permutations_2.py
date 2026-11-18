from typing import List
class Solution:

  def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()  # Duplicates saath laane ke liye
    used = [False] * len(nums)  # Visited indices track karne ke liye

    def backtrack(path):
      if len(path) == len(nums):  # Base case: permutation ready
        res.append(path[:])
        return

      for i in range(len(nums)):
        if used[i]:  # Pehle se used hai toh skip
          continue
        if (
            i > 0 and nums[i] == nums[i - 1] and not used[i - 1]
        ):  # Same level pe duplicate skip
          continue

        used[i] = True  # Choose
        path.append(nums[i])

        backtrack(path)  # Explore

        path.pop()  # Un-choose (Backtrack)
        used[i] = False

    backtrack([])
    return res

#Sorting + Backtracking (with Duplicate Pruning)

tc- O(N*N!) wc me sb elem unique so n! permut & copy O(n)
sc- O(n) recursion stack & used arr

