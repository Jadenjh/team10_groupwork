import numpy as np
import pandas as pd

def Sol(n,df):
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

main()