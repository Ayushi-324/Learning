class MinStack:

    def __init__(self):
        self.stack = []  # stack with pairs of val, ab tk curr_min
        
    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))  #agr stack khali phla element hi khud ka min
        else:
            curr_min = self.stack[-1][1]  #purane min aur naye val me chota no
            new_min = min(val, curr_min)
            self.stack.append((val, new_min))
        
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]   #top pair ka phla hissa value 
        
    def getMin(self) -> int:
        return self.stack[-1][1]  #top pair second hissa ab tk  ka min

#time - O(1) , space - O(n)
