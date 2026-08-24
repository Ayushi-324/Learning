class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 1. Agar koi bhi number "0" hai, toh answer 0 hoga
        if num1 == "0" or num2 == "0":
            return "0"
        
        # 2. Result array ka max size dono strings ki length ka sum hoga
        res = [0] * (len(num1) + len(num2))
        
        # 3. Strings ko ulta (reverse) karlo taaki peeche se multiply kar sakein
        num1, num2 = num1[::-1], num2[::-1]
        
        # 4. Ek-ek digit ko aapas me multiply karo
        for i in range(len(num1)):
            for j in range(len(num2)):
                # ASCII value use karke char ko int me badlo (bina int() function ke)
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                # multiply karke sahi index (i + j) par add karo
                product = digit1 * digit2
                res[i + j] += product
                
                # Carry ko aage bhej do aur current jagah par sirf single digit rakho
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
                
        # 5. Result ko wapas seedha karlo
        res = res[::-1]
        
        # 6. Shuruat ke faltu zeros (leading zeros) ko hatane ke liye loop
        start_idx = 0
        while start_idx < len(res) and res[start_idx] == 0:
            start_idx += 1
            
        # 7. Array ko wapas string me jod kar return kar do
        return "".join(map(str, res[start_idx:]))
