def bucketsort(arr, k):
    if len(arr) == 0:
        return arr

    max_val = max(arr)
    min_val = min(arr)
    bucket_size = (max_val - min_val) / k + 1
    buckets = [[] for _ in range(k)]

    for x in arr:
        i = int((x - min_val) / bucket_size)
        buckets[i].append(x)

    sorted_arr = []
    for i in range(k):
        sorted_arr.extend(sorted(buckets[i]))

    return sorted_arr

print(bucketsort([3, 1, 4, 2], 4))
print(bucketsort([5, 2, 9, 3, 6], 3))
print(bucketsort([], 5))