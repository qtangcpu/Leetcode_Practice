import math


def factorial_sum(n):
    s = 0
    while n>0:
        s+=math.factorial(n%10)
        n = n//10
    return s

def maxStrength(n):
    ans = [n]
    max_n = n
    while factorial_sum(n) not in ans:
        #print(1)
        #print(max_n)
        a = factorial_sum(n)
        ans.append(a)
        max_n = max(n,a)
        n = a
    return len(ans)*max_n

print(maxStrength(540))
