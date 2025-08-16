def fib_tab(n):
    # 여기에 코드를 작성하세요
    cache = [0 for _ in range(n+1)]
    cache[1] = 1
    cache[2] = 1
    
    if n > 2:
        for i in range(2, n+1):
            cache[i] = cache[i-1] + cache[i-2]
    
    return cache[n]
            

# 테스트 코드
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))