y = [1, 2, 3, 4, 4, 4, 5, 4, 3, 2, 3, 4, 5, 4]



def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
            print(arr[i])
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}


test = pick_peaks(y)

print(test)