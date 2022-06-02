import numpy as np
import pandas as pd

# 로그 관리
import logging

logger = logging.getLogger("main")
stream_hander = logging.StreamHandler()
logger.addHandler(stream_hander)

logger.setLevel(logging.DEBUG)

# 0,1,2,...,n-1 의 모든 순열(n!가지)을 (이중 list로) 반환 해주는 함수
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

# 솔루션 도출 함수 - 가능한 모든 순열 중 비용이 최소가 되는 순열 추출
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
    log = ""
    for i in range(0,n):
        log = "기계 " + df.index[i] + ": 작업 " + str(min_per[i]+1)
        logger.debug(log)
        f.write("기계 " + df.index[i] + "," + "작업 " + str(min_per[i]+1) + "\n")
    log = "최소비용 : " + str(min)
    logger.debug(log)
    f.write("최소비용," + str(min))
    f.close()

# main에서 데이터 생성 , n이 2미만 혹은 6초과 일 경우 예외 처리
def main():
    while True:
        n =int(input("숫자를 입력하세요: "))

        # 예외 처리 구문 (raise문)
        if n not in range(2,7):
            raise ValueError("2이상 6이하 숫자를 입력해주세요.")
        break

    #데이터 생성
    df = pd.DataFrame(np.random.randint(1, 11, size=(n, n)), index= list('ABCDEF')[:n], columns=  range(1,n+1))
    logger.debug(df)
    Sol(n,df)
main()