# 동적 프로그래밍
# 최적의 부분 구조 (Optimal Substructure) / 중복되는 부분 문제 (Overlapping Subproblem)

def fib_memo(n, cache):
    # 여기에 코드를 작성하세요
    if n in cache.keys():
        return cache[n]
    else:
        if n == 1 or n == 2:
            cache[n] = 1
            return cache[n]
        else:
            cache[n] = fib_memo(n-1,cache) + fib_memo(n-2,cache)
            return cache[n]
    


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트 코드
print(fib(10))
print(fib(50))
print(fib(100))
