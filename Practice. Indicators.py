def indicators(arr):
    indicator1 = 0
    indicator2 = 0
    left = 0
    right = 0
    while right < len(arr):
        while right < len(arr) and arr[right] == arr[left]:
            right += 1

        if right-left ==arr[left]:
            indicator1 +=1
            if left+1 ==arr[left]:
                indicator2 +=1
        left = right
    return indicator1-indicator2
