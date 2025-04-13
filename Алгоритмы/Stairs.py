def stairs(n):
    dp = [0 for i in range(n + 1)]
    dp[0] = 1
    for i in range(n):
        dp[i+1] += dp[i]
        if i + 2 < n + 1:
            dp[i+2] += dp[i]
    return dp[-1]
        
print(stairs(3))
