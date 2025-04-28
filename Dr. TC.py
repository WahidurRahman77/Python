t = int(input())
for _ in range(t):
    n = int(input ())
    s = input().strip()
    count = s.count('1')
    print(n + count *(n-2))