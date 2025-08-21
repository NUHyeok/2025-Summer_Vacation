def max_profit_memo(price_list, count, cache):
    # 여기에 코드를 작성하세요
    
    if count in cache:
        return cache[count]
    
    if count == 0:            
        cache[count] = 0
        return cache[count]
    
    if count == 1:
        cache[count] = price_list[1]
        return cache[count]
    
    
    best = price_list[count] if count < len(price_list) else 0
    
    for i in range(1, count // 2 + 1):
        best = max(best, max_profit_memo(price_list, i, cache) + max_profit_memo(price_list, count - i, cache))
    cache[count] = best
    return cache[count]
                    
                
        

    
def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트 코드
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
