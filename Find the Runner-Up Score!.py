if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    res = []
    [res.append(x) for x in arr if x not in res]
    n = len(res)
    res.sort()
    print(res[n-2])