class TrieNode:
    def __init__(self):
        self.children = {}  #har node ke ps uske child ki dict
        self.is_word = False  #check yha koi shabd khtm?
        
class WordDictionary:
    
    def __init__(self):
        self.root = TrieNode()  #rootnode before start dict

    def addWord(self, word: str) -> None:
        curr= self.root
        for char in word:
            if char not in curr.children:  #agr char phle se nhi toh naya node bana
                curr.children[char] = TrieNode()
            curr = curr.children[char] #aage bdho
        curr.is_word = True  #pura word khtm pr true mark
        
    def search(self, word: str) -> bool:
        def dfs(index, node):  #helper fn takes index of curr node and word 
            curr = node

            for i in range(index, len(word)):
                char = word[i]

                if char == ".": #agar . mile 
                    for child in curr.children.values(): #curr node ke jitne children sb pr check
                        if dfs(i+ 1, child): #agar kisi ek raste se bhi word mila return True
                            return True
                    return False  #ksii bhi child raste se no word found

                else: #agr normal char h 
                    if char not in curr.children: 
                        return False
                    curr = curr.children[char] #go to next node

            return curr.is_word  

        return dfs(0, self.root) #root node aur 0th index se search shuru
