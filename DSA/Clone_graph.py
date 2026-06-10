def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        map = {}   #dictionary to keep record ex-> {A: A', B: B', C: C'} and jb d pe aaye a already hai so no new connection c' -> a'

        def dfs(curr):   #WE ALWAYS DEFINE EDGE CASE IN RECURSION AT FIRST 
            if curr in map:
                return map[curr]   #agar duplicates ready hai toh vhi return ex if dfs(1) dobara aaya return mem[1]

            copy = Node(curr.val)   #naya duplicate banaya  Original: 1 and New copy: 1'
            map[curr] = copy     #Original 1  -> Copy 1' hasmhmap save 

            for neighbor in curr.neighbors:   #padosiyo se connections jode
                copy.neighbors.append(dfs(neighbor))   #ex- copy1.neighbors.append(copy2) so 1' -- 2'

            return copy 

        return dfs(node)        


# DFS/BFS + HashMap -> aisa ques linked list copy me bhi tha and i used hashmap there but here it's graph and to traverse in graph we're gonna use dfs here and hashmaps to avoid cycles 

#Seen before? Yes -> return copy......Not seen? Create copy then Save in hashmap and Clone neighbors

# TIME COMP - O(V+E) kyunki dfs deep me jata h and visit every node(vertices) and egdes once
#SPACE COMP -> O(V) as we used hashmap that stores like this....old1 -> copy1, old2 -> copy2
