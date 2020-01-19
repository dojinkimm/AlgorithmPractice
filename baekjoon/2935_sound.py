# BOJ 2935 - 소음
import sys
r = sys.stdin.readline

A = r().strip()
operator = r().strip()
B = r().strip()
zeros = '1'
if operator == '*':
    zeros += '0' * ((len(A)-1)+(len(B)-1))
else:
    max_len = max(len(A), len(B))-1
    min_len = min(len(A), len(B))-1
    if max_len != min_len:
        zeros += '0' * (max_len-min_len-1)+'1'+'0'*min_len
    else:
        zeros = '2' + '0'*max_len
print(zeros)