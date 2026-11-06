class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_len = 0
        
        # 1. Left-to-right pass to capture valid balances and closing overflows
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * right)  # Perfectly balanced
            elif right > left:
                left = right = 0                    # Reset: too many ')'
                
        left = right = 0
        
        # 2. Right-to-left pass to capture valid balances and opening overflows
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1
                
            if left == right:
                max_len = max(max_len, 2 * left)   # Perfectly balanced
            elif left > right:
                left = right = 0                    # Reset: too many '('
                
        return max_len
