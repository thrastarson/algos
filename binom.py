def binom(n, k):
    """
    Returns the binomial coefficient (n, k).
    Program uses a dynamic programming approach.
    """
    coeff = {}

    for i in range(n + 1):
        coeff[i] = {}
        coeff[i][0] = 1

    for j in range(k + 1):
        coeff[j][j] = 1

    for i in range(1, n + 1):
        for j in range(1, i):
            print(i, j)
            coeff[i][j] = coeff[i-1][j-1] + coeff[i-1][j]

    return coeff[n][k]

if __name__ == '__main__':
    print(binom(5, 4))
