class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # held: stock paas hai, sold: aaj becha, reset: cooldown/rest phase
        held, sold, reset = float('-inf'), float('-inf'), 0
        
        for price in prices:
            prev_sold = sold
            sold = held + price          # Aaj becha = pehle se held tha + aaj ka price mila
            held = max(held, reset - price) # Aaj kharida = cooldown ke baad bache paise - price
            reset = max(reset, prev_sold) # Aaj rest kiya = kal ka max rest ya kal jo becha tha

        return max(sold, reset) # Last me profit tabhi hoga jab hath me koi stock na ho
