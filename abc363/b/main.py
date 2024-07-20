def a(n, t, p, lengths):
    current_count = sum(1 for length in lengths if length >= t)
    
    if current_count >= p:
        return 0
    
    days = 0
    while current_count < p:
        days += 1
        current_count = sum(1 for length in lengths if length + days >= t)
        
    return days

n, t, p = map(int, input().split())
lengths = list(map(int, input().split()))

print(a(n, t, p, lengths))



