'''
問題集
URL:https://atcoder.jp/contests/tessoku-book/tasks
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cb
B問題
'''
#入力
N = int(input())
A = list(map(int, input().split()))
#出力
import itertools
a = 0
for n in itertools.combinations(A,3):
    three_no_total = sum(n)
    if (three_no_total) ==1000:
        print('Yes')
        a += 1
        break
    else : 
        three_no_total = 0
if a == 0:
    print('No')

        




     
    
    
    
    
        