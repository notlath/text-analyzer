from utils import tokenize

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        elif left[i] > right[j]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def common_words_dc(text1, text2):
    # Tokenize and get unique words
    tokens1 = tokenize(text1)
    tokens2 = tokenize(text2)
    uniq1 = list(set(tokens1))
    uniq2 = list(set(tokens2))
    # Sort using divide and conquer merge sort
    sorted1 = merge_sort(uniq1)
    sorted2 = merge_sort(uniq2)
    # Merge to find intersection
    common = []
    i = j = 0
    while i < len(sorted1) and j < len(sorted2):
        if sorted1[i] == sorted2[j]:
            common.append(sorted1[i])
            i += 1
            j += 1
        elif sorted1[i] < sorted2[j]:
            i += 1
        else:
            j += 1
    return common
