"""
Ｓｋｙ株式会社プログラミングコンテスト2023（AtCoder Beginner Contest 289）
URL: https://atcoder.jp/contests/abc289/tasks/abc289_a
"""

N = int(input())
#if N % 100 == 0:
STR = list(map(int,str(N)))
result = N*1.1
ans = list(map(str,str(result)))
#if N >= 91000 and N<100000:
#    print(''.join(ans[:(len(STR))+1]))
print(''.join(ans[:(len(STR))]))

#1問WA