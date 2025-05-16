def main():
    import sys
    input = sys.stdin.read 
    data = input().split()
    t = int(data[0])
    index = 1
    
    for _ in range(t):
        n = int(data[index])
        x = int(data[index+1])
        index += 2
        if x == 0:
            perm = list(range(1, n)) + [0]
        elif x == n:
            perm = list(range(n))
        else:
            part1 = list(range(x))
            part2 = list(range(x+1, n))
            perm = part1 + part2 + [x]
        print(' '.join(map(str, perm)))
    
if __name__ == "__main__":
    main()
