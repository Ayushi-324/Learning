class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()  #sort arr dup sath me la

        def backtrack(i, curr_combination, curr_sum):
            if curr_sum == target:
                res.append(list(curr_combination))
                return
            if curr_sum > target or i == len(candidates):
                return

            curr_combination.append(candidates[i]) #Elem liya (i + 1 kr taaki repeat nhi)
            backtrack(i + 1, curr_combination, curr_sum + candidates[i]) 
            curr_combination.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: #Elem skip kr(Sare dup bhi skip)
                i += 1
            backtrack(i + 1, curr_combination, curr_sum)

        backtrack(0, [], 0)
        return res

#BACKTRACKING (subsets with dup/ decision tree)      t- O(2^N) hr elem 2 choice   s- O(n) no hashset
