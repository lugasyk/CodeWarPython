def maxSequence(arr):
    maximum = 0
    local_maximum = 0
    for i in arr:
        if local_maximum > 0:
            local_maximum += i
            if local_maximum < 0:
                local_maximum = 0
            elif local_maximum > maximum:
                maximum = local_maximum
        elif i > 0:
            local_maximum += i

    return maximum