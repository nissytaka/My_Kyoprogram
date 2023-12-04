'''
CodeQUEEN 2023 予選 (AtCoder Beginner Contest 308)
URL:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ca
C問題
'''
#入力

'''
問題集
URL:https://atcoder.jp/contests/tessoku-book/tasks
URL:https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ca
B問題
'''
#入力
A,B = map(int, input().split())
#出力
C = []
a = 0
for i in range(A,B+1):
    if 100%i == 0:
        a += 1
        print('Yes')
        break
if a == 0:
    print('No')
