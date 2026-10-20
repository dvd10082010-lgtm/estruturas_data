def quicksort(arr):
    if len(arr) < 2:
        return arr
    
    pivot = arr[len(arr) // 2]
    equals = [x for x in arr if x == pivot]
    minor = [x for x in arr if x < pivot]
    moreless = [x for x in arr if x > pivot]

    return quicksort(minor) + equals + quicksort(moreless)   
