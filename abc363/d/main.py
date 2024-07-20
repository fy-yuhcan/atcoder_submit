def p(N):
    count = 0
    num = 1
    
    def g(length):
        if length == 1:
            for i in range(10):
                yield i
        else:
            half_len = (length + 1) // 2
            start = 10**(half_len - 1)
            end = 10**half_len
            for i in range(start, end):
                s = str(i)
                if length % 2 == 0:
                    yield int(s + s[::-1])
                else:
                    yield int(s + s[-2::-1])
    
    length = 1
    while True:
        for pal in g(length):
            count += 1
            if count == N:
                return pal
        length += 1

N = int(input().strip())
print(p(N))
