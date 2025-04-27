'''
問題集
URL:https://atcoder.jp/contests/tessoku-book/tasks
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cg
B問題
'''
#入力
N=int(input())
list_A=[list(map(int, input().split())) for _ in range(N)]
Q=int(input())
list_B=[list(map(int, input().split())) for _ in range(Q)]


#出力
for j in list_B:
    a=0
    for i in list_A:
        if i[0]>=j[0] and i[0]<=j[2] and i[1]>=j[1] and i[1]<=j[3]:
            a+=1
    print(a)
