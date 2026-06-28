class TrieNode: #trienode CLASS-> contains two things,  children -ek  khali dict{} 26 letter store , is_end - flag(false) jo true tb hoga jb koi word vha khatam     
    def __init__(self):
        self.children = {}  #LTEER -> next trienode
        self.is_end = False  # kya yha koi word khatam hota h ?
        
class Trie:  #Trie class -> main manager contains root node jha se sb start 
    def __init__(self):
        self.root = TrieNode() #main starting point 

    def insert(self, word: str) -> None: #root pr khade hoke word ke ek ek letter pr loop chlega 
        curr = self.root
        for char in word: #kya x abhi ke node ke children me h? 
            if char not in curr.children:
                curr.children[char] = TrieNode()  #naya letter node bnao ex - a p p l e 
            curr = curr.children[char]  #us node ke andr ghuso 
        curr.is_end = True   #word khatam -> flag true (last node ex- e in apple pr jakar true mark)
 
    def search(self, word: str) -> bool: # ex - searching app me letters toh milenge pr node p r is_end false as word was apple 
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False  #letter nhi mila means word nhi h 
            curr = curr.children[char]
        return curr.is_end  #pura word mila and waha khatam bhi hona chahiye 
    
    def startsWith(self, prefix: str) -> bool: #checking prefix - bs itna check krna h ki letters mil rhe h ya nhi 
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False  #prefix letters hi break hogye 
            curr = curr.children[char]
        return True   #sare letters mil gye prefix matches 

# PREFIX TREE via Nesting Dictionaries , TIME - insert O(L) l is len of word, search/starts with - O(l) fast string searching,  SPACE - O(n*l) in worst case we store n words of len L inside tree nodes


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
