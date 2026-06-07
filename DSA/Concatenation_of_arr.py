class Solution:
    def getConcatenation(self, nums):
        return nums + nums

#nums + nums -> pure arr ko copy krke naya arr banata hai but if i wanna do this with loops....
# firstly i thought make a copy in python but let's say n = 3 copy me 6 bnenge baki 3 me kya values dalu ? then after trying my weird maths logics i got remainder(modular math %) isse index wapas ghum rha hai ..
n = len(nums)
ans  = [0] * (n * k) # list jisme filhaal 0 hai and * 2*n me vo list utni baar repeat so ans = [0,0,0,0,0,0]
for i in range (n*k):  # single loop pure bade arr like 0-5 tk
  ans [i] = nums[i % n]  #index always 0 se n-1 ke beech me ghumta 
return ans  

#time and space = O(n*k) as naya bada arr  
#0 % 3 = 0 (Index 0)1 % 3 = 1 (Index 1)2 % 3 = 2 (Index 2)3 % 3 = 0 (Wapas Index 0 par aa gaye )4 % 3 = 1 index 1 USE THIS% -> Kisi bhi loop ko gol-gol ghumane ke liye
