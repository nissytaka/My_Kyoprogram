'''
B問題
URL:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ca
'''
#入力
a,b = map(int,input().split())
#出力
N=0
for i in range(a,b+1):
    if 100%i ==0:
        N +=1
if N>0:
    print("Yes")
else:
    print("No")