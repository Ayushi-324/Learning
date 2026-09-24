import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        # Append original index to track them: [enqueue, process, index]
        ext_tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        
        res, min_heap = [], []
        time, i, n = 0, 0, len(tasks)
        
        while i < n or min_heap:
            # 1. If heap empty and current time < next task arrival, fast-forward time
            if not min_heap and time < ext_tasks[i][0]:
                time = ext_tasks[i][0]
                
            # 2. Push all available tasks at current time into Min-Heap
            while i < n and ext_tasks[i][0] <= time:
                heapq.heappush(min_heap, (ext_tasks[i][1], ext_tasks[i][2])) # (process_time, index)
                i += 1
                
            # 3. Process the shortest job
            proc_time, idx = heapq.heappop(min_heap)
            time += proc_time
            res.append(idx)
            
        return res

        
