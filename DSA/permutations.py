class Solution:
    def permute(self, nums):
        result = []

        def backtrack(current_path):
            if len(current_path) == len(nums):
                result.append(current_path[:])
                return

            for n in nums:
                if n not in current_path:
                    current_path.append(n)
                    backtrack(current_path)
                    current_path.pop()

        backtrack([])
        return result
