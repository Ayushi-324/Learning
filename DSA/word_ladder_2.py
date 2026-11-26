from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        # Forward BFS: Sirf shortest distance (level) aur parent links save karo
        parents = defaultdict(list)
        level = {beginWord}
        wordSet.discard(beginWord)
        found = False
        
        while level and not found:
            next_level = set()
            for word in level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nxt = word[:i] + c + word[i+1:]
                        if nxt in wordSet:
                            if nxt == endWord:
                                found = True
                            next_level.add(nxt)
                            parents[nxt].append(word) # Ulta edge: child -> parent
            wordSet -= next_level # Pure level ke baad delete karo
            level = next_level
            
        if not found:
            return []
            
        # Backward DFS (endWord -> beginWord): Dead-ends par kabhi nahi jayega
        res = []
        def dfs(curr: str, path: List[str]):
            if curr == beginWord:
                res.append(path[::-1]) # Path reverse karke add karo
                return
            for p in parents[curr]:
                path.append(p)
                dfs(p, path)
                path.pop()
                
        dfs(endWord, [endWord])
        return res




Forward BFS + Backward DFS

tc- O(n*l2+p*l)  sc- O(n*l) 
