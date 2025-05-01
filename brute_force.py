from utils import clean_text

def count_occurrences(text, pattern):
    """Count occurrences of pattern in text using brute-force substring search."""
    txt = clean_text(text)
    pat = clean_text(pattern)
    count = 0
    n, m = len(txt), len(pat)
    for i in range(n - m + 1):
        if txt[i:i+m] == pat:
            count += 1
    return count
