"""
Ｓｋｙ株式会社プログラミングコンテスト2023（AtCoder Beginner Contest 289）
URL: 
"""
#入力
N = int(input())
#出力
if N % 100 == 0:
    STR = list(map(int,str(N)))
    result = N*1.10
    ans = list(map(str,str(result)))
    print(''.join(ans[:(len(STR))]))


#1問WA