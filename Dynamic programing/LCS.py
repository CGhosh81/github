def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for i in range(m + 1)]
    # Build the L array in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 0 or j == 0 :  
              L[i][j] = 0 
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                # print(Y[j-1])
                print(X[i-1])
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
                
    # L[m][n] contains the length of the LCS
   
    return L[m][n]
# Test the function
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is", lcs(X, Y))
