def monoton(arr):  
    first_fails = last_fails = None
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

        if not increasing and not decreasing:
            if first_fails is None:
                first_fails = (i - 1, arr[i - 1])
            last_fails = (i, arr[i])

    return first_fails, last_fails

arr = [1, 3, 2, 4, 5, 6, 8, 7, 9, 10]
print(monoton(arr))
