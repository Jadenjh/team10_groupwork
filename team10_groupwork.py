import numpy as np
import pandas as pd

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

    df.to_csv('output/result.csv',index = True)
    f = open('output/result.csv', 'a')
    for i in range(0,n):
        print("기계 " + df.index[i] + ": 작업", min_per[i]+1)
        f.write("기계 " + df.index[i] + "," + "작업 " + str(min_per[i]+1) + "\n")
    print("최소비용 :", min)
    f.write("최소비용," + str(min))
    f.close()


def main():
    while True:
        n =int(input("숫자를 입력하세요: "))
        if n < 2 or n > 6:
            n = int(input("숫자를 입력하세요: "))
        else:
            break

    df = pd.DataFrame(np.random.randint(1, 11, size=(n, n)), index= list('ABCDEF')[:n], columns=  range(1,n+1))
    print(df)
    Sol(n,df)
main()