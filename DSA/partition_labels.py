class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        # 1. Har character ka last index save karo
        last_seen = {char: i for i, char in enumerate(s)}
        
        partitions = []
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            # 2. Window ko badhao jahan tak current char ka last index hai
            end = max(end, last_seen[char])
            
            # 3. Agar current index end par pahunch gaya, matlab partition complete
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1  # Agle partition ka start pointer set karo
                
        return partitions
