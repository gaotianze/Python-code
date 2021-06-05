# Label-correcting Algorithm By TianzeGao 20210605
def label_correcting(A):
    n=len(A)
    d_i={1:0}
    for j in range(1, n):
        d_i[j + 1]=99 # 初始化

    for i in range(1, n+1):
        now_node=i
        pre_len=d_i[i]
        for j in range(0, n):
            if A[now_node - 1][j] != 0 and A[now_node - 1][j] != 999:
                d_i[j + 1] = min(A[now_node - 1][j] + pre_len, d_i[j + 1])  # min[d(j)+Cij, d(j)]
    print(d_i)

if __name__ == '__main__':
    # 以999代表∞
    A = [[0, 6, 4, 999, 999, 999],
         [999, 0, 2, 2, 999, 999],
         [999, 999, 0, 1, 2, 999],
         [999, 999, 999, 0, 999, 7],
         [999, 999, 999, 1, 0, 3],
         [999, 999, 999, 999, 999, 0]]

    '''A = [[0,1,2,999,999,999],
         [999,0,7,3,999,999],
         [999,999,0,999,5,999],
         [999,999,5,0,10,13],
         [999,999,999,999,0,4],
         [999,999,999,999,999,0]]'''  # 备用测试案例

    label_correcting(A)
