class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        target = threshold * k
        curr_s = sum(arr[:k])
        count = 0

        if curr_s >= target:
            count += 1

        for i in range(k, len(arr)):
            curr_s += arr[i] - arr[i-k]
            if curr_s >= target:
                  count += 1

        return count
        
