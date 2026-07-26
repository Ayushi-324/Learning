class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()  #pop phle do elements comp ek bar me do elem pr operation
                a = stack.pop()   #second pop

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a *b)
                elif token == '/':
                    stack.append(int(a/b))
            else:
                stack.append(int(token))  #to avoid floats 

        return stack[0]

#STACK/ LIFO   time- O(n)  space- O(n) wc me all no stack me store
# LOGIC - jab tk no mile dal stack me -> operator aate hi pichle do no pop kr calculation kr unpe -> wapas stack me dal de 
