import numpy as np
import pandas as pd

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