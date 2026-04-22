class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Use amount + 1 as a sentinel "infinity" value
        # since we can never need more than amount coins to make any sum
        dp = [amount + 1] * (amount + 1)
        
        # Base case: 0 coins needed to make amount 0
        dp[0] = 0

        # Build up solutions from amount 1 to target amount
        for current_amount in range(1, amount + 1):
            # Try every coin and take the best (minimum) option
            for coin in coins:
                if current_amount - coin >= 0:
                    # If we use this coin, we need 1 + however many coins
                    # were needed for the remaining amount
                    dp[current_amount] = min(
                        dp[current_amount],
                        dp[current_amount - coin] + 1
                    )

        # If dp[amount] is still the sentinel value, no solution exists
        return dp[amount] if dp[amount] != amount + 1 else -1