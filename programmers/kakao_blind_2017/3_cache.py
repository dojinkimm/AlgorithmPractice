def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5   
    
    answer = 0
    cache = []
    
    for city in cities:
        city = city.lower()
        if city not in cache:
            if len(cache) == cacheSize: # cache 꽉 찼으면 하나를 제거한다, 제일 마지막이 LRU
                cache.pop()
            answer += 5  # cache에 없으면 5를 더한다
        else:
            cache.pop(cache.index(city)) # 기존 item을 제거한다
            answer += 1 # cache hit 이기 때문에 1을 더한다
            
        cache.insert(0,city) # 가장 최근에 사용된 것을 맨 앞에 추가한다
            
    return answer