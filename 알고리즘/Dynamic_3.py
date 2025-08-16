def fib_optimized(n):
    # 여기에 코드를 작성하세요
    current = 1
    previous = 1
    
    if n <= 2:
        return 1
    
    else:
        for _ in range(3,n+1):
            temp = current
            current = temp + previous
            previous = temp
            
    return current


# 테스트 코드
print(fib_optimized(16))
print(fib_optimized(53))
print(fib_optimized(213))
