def perfect_content_selection(contents, max_length):
    n = len(contents)
    # create a DP table where dp[i][j] represents the maximum quality score
    # achievable with the first i contents and a max length of j
    dp = [[0] * (max_length + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        length, quality = contents[i-1]
        for j in range(max_length + 1):
            if length <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-length] + quality)
            else:
                dp[i][j] = dp[i-1][j]

    # the maximum quality score is found at dp[n][max_length]
    return dp[n][max_length]
