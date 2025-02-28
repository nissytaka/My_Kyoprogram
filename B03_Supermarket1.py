'''
CodeQUEEN 2023 予選 (AtCoder Beginner Contest 308)
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cb
B問題
'''
#入力
N=int(input())
list = list(map(int,input().split()))
#出力
import itertools
a=0
for i in (itertools.combinations(list,3)):
    answer=sum(i)
    if answer ==1000:
        a+=1
if a>0:
    print("Yes")    
else:  
    print("No")    
