import collections

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Har task ki frequency (count) nikaalo
        count = collections.Counter(tasks)
        
        # Sabse zyada aane waale task ki frequency dhoondo (e.g., A agar 3 baar aaya hai)
        max_freq = max(count.values())
        
        # Sabse frequent task ke beech mein khali slots (blocks) kitne banenge
        # Agar A 3 baar hai, toh blocks = (3 - 1) = 2. Har block ka size = n + 1
        chunks_time = (max_freq - 1) * (n + 1)
        
        # Check karo ki kitne aur tasks hain जिनकी frequency bilkul max_freq ke barabar hai
        # Kyunki wo log last wale block ke baad aakhri mein extra slots lenge
        max_freq_tasks_count = sum(1 for value in count.values() if value == max_freq)
        
        # Total formula-based slots calculates karein
        calculated_slots = chunks_time + max_freq_tasks_count
        
        # Agar slots kam pad rahe hain tasks se, toh bina idle time ke saare tasks arrange ho jayenge.
        # Isiliye dono ka maximum return karenge.
        return max(calculated_slots, len(tasks))
