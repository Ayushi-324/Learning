class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = 0
        current_end = 0  # Current jump ki maximum reach
        farthest = 0     # Agle jump se kitna door ja sakte hain
        
        # Last index tak pahunchne ke baad jump nahi karna, isliye len(nums) - 1
        for i in range(len(nums) - 1):
            # Har step par max reach update karo
            farthest = max(farthest, i + nums[i])
            
            # Jab current jump ki limit khatam ho jaye, jump lo
            if i == current_end:
                jumps += 1
                current_end = farthest  # Nayi limit set karo
                
                # Agar pehle hi end tak pahunch sakte hain toh break karo
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps


#GREEDY APPROACH  as dp O(n2) but here har range  me best possible next jump phle track    tc- O(N) arr traverse once      sc- O(1) 
