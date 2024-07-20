def a(s):
    return s == s[::-1]

def b(s, start, end, result):
    if start == end:
        result.add(''.join(s))
    else:
        for i in range(start, end + 1):
            s[start], s[i] = s[i], s[start]
            b(s, start + 1, end, result)
            s[start], s[i] = s[i], s[start]

def c(n, k, s):
    result = set()
    s_list = list(s)
    b(s_list, 0, n - 1, result)
    
    count = 0
    for perm in result:
        contains_palindrome = False
        
        for i in range(n - k + 1):
            if a(perm[i:i + k]):
                contains_palindrome = True
                break
        
        if not contains_palindrome:
            count += 1
    
    return count

n, k = map(int, input().split())
s = input().strip()
print(c(n, k, s))
