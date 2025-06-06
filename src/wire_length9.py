import math

def max_wire_length(w, heights):
    n = len(heights)
    dp = [[0, 0] for _ in range(n)]

    for i in range(1, n):
        for h1 in [0, 1]:
            for h2 in [0, 1]:
                height1 = 1 if h1 == 0 else heights[i - 1]
                height2 = 1 if h2 == 0 else heights[i]
                length = math.hypot(w, height2 - height1)
                dp[i][h2] = max(dp[i][h2], dp[i - 1][h1] + length)

    return round(max(dp[-1]), 2)
