from utils import clean_text, tokenize

def kmp_search_positions(text, pattern):
    """Return list of start indices of pattern in text using Knuth-Morris-Pratt algorithm."""
    txt = clean_text(text)
    pat = clean_text(pattern)
    n, m = len(txt), len(pat)
    if m == 0 or m > n:
        return []
    # Build LPS array
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    # Search pattern
    positions = []
    i = j = 0
    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1
            if j == m:
                positions.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return positions

def jump_search_in_text(text, key):
    """Search for key in sorted tokens using Jump Search. Returns index in sorted list or -1 if not found."""
    tokens = sorted(tokenize(text))
    n = len(tokens)
    if n == 0:
        return -1
    step = int(n ** 0.5) or 1
    # Find the block where key may be
    prev = 0
    while prev < n and tokens[min(n - 1, prev + step)] < key:
        prev += step
    # Linear search within the block starting at prev
    end = min(prev + step + 1, n)
    for idx in range(prev, end):
        if tokens[idx] == key:
            return idx
    return -1