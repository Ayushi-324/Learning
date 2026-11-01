class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            # Return cached result if already calculated
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base Case: If pattern is exhausted, text must also be exhausted
            if j == len(p):
                return i == len(s)

            # Check if current characters match (handling the '.' wildcard)
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # Handle the '*' wildcard if the next character in pattern is '*'
            if (j + 1) < len(p) and p[j + 1] == '*':
                # Choice 1: Don't use '*' (skip character and '*'). 
                # Choice 2: Use '*' (if current chars match, move text pointer 'i' forward)
                memo[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
                return memo[(i, j)]

            # Normal matching step if no '*' follows
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]

            # Characters do not match
            memo[(i, j)] = False
            return False

        return dfs(0, 0)
