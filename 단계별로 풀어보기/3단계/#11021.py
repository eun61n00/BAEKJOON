#11021 A+B - 7

#https://www.acmicpc.net/problem/11021

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print("Case #", i+1, ": ", a+b)
