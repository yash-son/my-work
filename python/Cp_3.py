def longest_common_subsequence(X, Y):
    # Length of input strings
    m = len(X)
    n = len(Y)

    # Create a 2D DP table initialized with 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # Characters match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # Characters do not match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtracking to find the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:  # Characters match
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # Move towards the larger value
            i -= 1
        else:
            j -= 1

    # The LCS is built in reverse order
    lcs.reverse()
    return ''.join(lcs)

# Example usage

X = "AGGTAB"
Y = "GXTXAYB"

lcs = longest_common_subsequence(X, Y)
print(f"The Longest Common Subsequence is: {lcs}")

print((((int(input("Enter rollnum: "))-1)//4)%3)+1)
