class Solution:
    def groupAnagrams(self, strs):
        memory = {}

        for word in strs:
            label = "".join(sorted(word))

            if label not in memory:
                memory[label] = []

            memory[label].append(word)

        return list(memory.values())
