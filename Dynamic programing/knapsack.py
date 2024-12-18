def knapSack(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0
    # If weight of the nth item is more than Knapsack capacity W, it cannot be included
    if wt[n - 1] > W:
        return knapSack(W, wt, val, n - 1)
    # Return the maximum of two cases:
    # (1) nth item included
    # (2) nth item not included
    else:
        return max(
            val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
            knapSack(W, wt, val, n - 1)
        )
# Driver Code
profit = [60, 100, 120]
weight = [10, 20, 30]
W = 50
n = len(profit)
# Print the result
print("Maximum profit:", knapSack(W, weight, profit, n))
