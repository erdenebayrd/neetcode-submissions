class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # time: O(n * amount)
        # space: O(n * amount)
        # method: DP bottom up
        n = len(coins)
        
        """
            0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ............ amount
        0.  1       
        1.  1
        2.  1                   [x]
        3.  1
        4.  1
        5.  1
        ....
        ....
        ....
        ....
        ....
        n - 1



        dp[i][cur_amount] = dp[i - 1][cur_amount] + dp[i][cur_amount - coins[i]]
        """

        dp = [[0] * (amount + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        
        for i in range(n):
            for cur_amount in range(1, amount + 1):
                if i - 1 >= 0:
                    dp[i][cur_amount] += dp[i - 1][cur_amount]
                if cur_amount - coins[i] >= 0:
                    dp[i][cur_amount] += dp[i][cur_amount - coins[i]]
        
        return dp[n - 1][amount]


