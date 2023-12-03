'''
問題集
URL:https://atcoder.jp/contests/tessoku-book/tasks
URL: https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cc
B問題
'''
#入力
N = int(input())
#出力
N_list = list(map(int, str(N)))
a = 0
for i in range(len(N_list)):
    a += N_list[-(i+1)]*2**i
print(a)