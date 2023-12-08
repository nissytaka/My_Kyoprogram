'''
問題集
URL:https://atcoder.jp/contests/tessoku-book/tasks
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ce
B問題
'''
#入力
N = int(input())
A = list(map(int, input().split())) 
Q =int(input())
L_R = [list(map(int, input().split())) for _ in range(Q)]
#出力 
a = []
b = 0
b2 = 0
b3 = 0
for i in A:
    b += i
    a.append(b)
for n in L_R:
    b2 = a[n[1]-1]-a[n[0]-1]
    b3 = (n[1]+1-n[0])/2
    if A[n[0]-1] == 1:
        b2 += 1  
    if b2>b3:
        print('win')
    elif b2 == b3 :
        print('draw')
    else :
       print('lose')
