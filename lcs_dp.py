from utils import tokenize

def longest_common_subsequence(seq1, seq2):
    # Build DP table
    m, n = len(seq1), len(seq2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if seq1[i] == seq2[j]:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    # Reconstruct LCS
    i, j = 0, 0
    lcs_seq = []
    while i < m and j < n:
        if seq1[i] == seq2[j]:
            lcs_seq.append(seq1[i])
            i += 1
            j += 1
        elif dp[i+1][j] >= dp[i][j+1]:
            i += 1
        else:
            j += 1
    return lcs_seq

def lcs_from_texts(text1, text2):
    # Tokenize input texts and compute LCS
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)
    return longest_common_subsequence(tokens1, tokens2)
