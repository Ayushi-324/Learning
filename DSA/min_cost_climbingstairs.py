class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)  #Top floor pe pahunchne ka cost 0 hai.

        for i in range(len(cost) - 3, -1, -1):   #Peeche se start karke har step ka min cost nikalenge.
            cost[i] += min(cost[i + 1], cost[i + 2])   #Agle 1 ya 2 step me se jo sasta hai, use add karo.


        return min(cost[0], cost[1])  # Index 0 ya 1 jahan se bhi kam kharcha ho, wahan se start karo.
        
