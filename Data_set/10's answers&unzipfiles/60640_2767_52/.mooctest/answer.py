
def coin_change_dp(arr, N):
    col = N+1
    row = len(arr) + 1
    dp = [[0 for x in range(col)] for x in range(row)]
    for i in range(row):
        dp[i][0] = 1
    for r in range(0, row):
        for c in range(1, col):
            if r == 0 and col > 0:
                dp[r][c] = 0
            else:
                 # Excluding r  (r dipicts coins)
                x = dp[r-1][c]

                # Including r
                y = dp[r][c-arr[r-1]] if (c - arr[r - 1]) >= 0 else 0

                dp[r][c] = x + y
                #dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[row-1][col-1]


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        v = int(input())
        print(coin_change_dp([3, 5, 10], v))
