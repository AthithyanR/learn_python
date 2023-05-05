def merge_sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr
        return [arr[1], arr[0]]
    
    mid = len(arr) // 2
    left = merge_sort(arr[0:mid])
    right = merge_sort(arr[mid:])

    ret = []
    l = 0
    r = 0

    while(l < len(left) and r < len(right)):
        if left[l] < right[r]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1

    while(l < len(left)):
        ret.append(left[l])
        l += 1

    while(r < len(right)):
        ret.append(right[r])
        r += 1

    return ret

print(merge_sort([5, 4, 9, 1, 100, -1]))
