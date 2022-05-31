def Sol(n,df):
    df.to_csv('output/result.csv',index = True)
    f = open('output/result.csv', 'a')
    for i in range(0,n):
        print("기계 " + df.index[i] + ": 작업", min_per[i]+1)
        f.write("기계 " + df.index[i] + "," + "작업 " + str(min_per[i]+1) + "\n")
    print("최소비용 :", min)
    f.write("최소비용," + str(min))
    f.close()
