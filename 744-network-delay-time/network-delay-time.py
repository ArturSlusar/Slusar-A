import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Строим граф
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v, w))
            
        pq = [(0, k)]  # (текущее_время, узел)
        seen = set()
        ans = 0
        
        while pq:
            t, u = heapq.heappop(pq)
            
            # Если уже были здесь более коротким путем, пропускаем
            if u in seen:
                continue
                
            seen.add(u)
            ans = max(ans, t) # Обновляем максимальное время
            
            # Добавляем соседей в очередь
            for v, w in g[u]:
                if v not in seen:
                    heapq.heappush(pq, (t + w, v))
                    
        return ans if len(seen) == n else -1
        