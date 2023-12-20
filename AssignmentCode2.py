import numpy as np

def HS(x, y, Matrix):
    n = len(x)
    m = len(y)

    dp = np.zeros((n + 1, m + 1))

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = dp[i - 1][j - 1] + Matrix[x[i - 1]][y[j - 1]]
            delete = dp[i - 1][j] + Matrix[x[i - 1]]['-']
            insert = dp[i][j - 1] + Matrix['-'][y[j - 1]]

            dp[i][j] = max(match, delete, insert)

    aligned_x = ''
    aligned_y = ''
    i, j = n, m

    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + Matrix[x[i - 1]][y[j - 1]]:
            aligned_x = x[i - 1] + aligned_x
            aligned_y = y[j - 1] + aligned_y
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + Matrix[x[i - 1]]['-']:
            aligned_x = x[i - 1] + aligned_x
            aligned_y = '-' + aligned_y
            i -= 1
        else:
            aligned_x = '-' + aligned_x
            aligned_y = y[j - 1] + aligned_y
            j -= 1

    return aligned_x, aligned_y

scoring_matrix = {
    'A': {'A': 1, 'G': -0.8, 'T': -0.2, 'C': -2.3, '-': -0.6},
    'G': {'A': -0.8, 'G': 1, 'T': -1.1, 'C': -0.7, '-': -1.5},
    'T': {'A': -0.2, 'G': -1.1, 'T': 1, 'C': -0.5, '-': -0.9},
    'C': {'A': -2.3, 'G': -0.7, 'T': -0.5, 'C': 1, '-': -1},
    '-': {'A': -0.6, 'G': -1.5, 'T': -0.9, 'C': -1, '-': 0}
}

x = "ATGCC"
y = "TACGCA"

aligned_x, aligned_y = HS(x, y, scoring_matrix)
print("Highest Score:")
print(aligned_x)
print(aligned_y)
