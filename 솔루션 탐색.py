def permute(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

def Sol(n,df):
    arr = [i for i in range(n)]
    per = permute(arr)
    min = 999
    min_per = []
    for p in range(0,len(per)):
        sum = 0
        for x in range(0,n):
            sum += df.iloc[x,per[p][x]]
        if sum < min:
            min = sum
            min_per = per[p]