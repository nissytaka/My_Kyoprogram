'''
CodeQUEEN 2023 予選 (AtCoder Beginner Contest 308)
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cb
B問題
'''
#入力
N = int(input())
A = list(map(int, input().split()))
#出力
import itertools
total = sum(A)
a = 0
for n in itertools.combinations(A,N-3):
    two_no_total = sum(n)
    if (total-two_no_total) ==1000:
        print('Yes')
        a += 1
        break
    else : 
        two_no_total = 0
if a == 0:
    print('No')
