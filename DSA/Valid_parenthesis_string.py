 def checkValidString(self, s: str) -> bool:
        min_open = 0  # wants to pick less brackets when * comes throw brackets 
        max_open = 0  #will pick most brackets for * becomes greedy and picks one more bracket

        for char in s:
            if char == '(':   
                min_open += 1
                max_open += 1
            elif char == ')':
                min_open -= 1
                max_open -= 1
            elif char == '*':  # max +1 best case and min -1 for worst 
                min_open -= 1
                max_open += 1
            if max_open < 0:   #means no balance as rule ke acc () ye dono chahiye 
                return False

            if min_open < 0:  # as it can't have negative value and * ko khali "" le lenge 
                min_open = 0

        return min_open == 0 #if min open 0 so string valid 

# as wildcard * is there in ques so idk exactly if i wanna make (, ), or empty even i thought for stack and recursion but that is too slow so exact value nhi range track ....
  #max_open me agr hr * ko ( open man le toh kitne open brackets increase agar har * ko close mane so kitne open brackets kam         
