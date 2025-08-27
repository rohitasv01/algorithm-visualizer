import random, heapq, collections

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    steps = []
    for i in range(n):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                steps.append(a.copy())
    return a, steps

def insertion_sort(arr):
    a = arr.copy()
    steps = []
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >=0 and key < a[j] :
                a[j+1] = a[j]
                j -= 1
                steps.append(a.copy())
        a[j+1] = key
        steps.append(a.copy())
    return a, steps

def merge_sort(arr):
    steps = []
    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        steps.append(merged.copy())
        return merged
    def _merge(a):
        if len(a) <= 1:
            return a
        mid = len(a)//2
        left = _merge(a[:mid])
        right = _merge(a[mid:])
        return merge(left, right)
    sorted_a = _merge(arr.copy())
    return sorted_a, steps

def quick_sort(arr):
    a = arr.copy()
    steps = []
    def _quick(a, low, high):
        if low < high:
            p = partition(a, low, high)
            steps.append(a.copy())
            _quick(a, low, p-1)
            _quick(a, p+1, high)
    def partition(a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i+1], a[high] = a[high], a[i+1]
        return i+1
    _quick(a, 0, len(a)-1)
    return a, steps

def heap_sort(arr):
    a = arr.copy()
    heapq.heapify(a)
    sorted_a = [heapq.heappop(a) for _ in range(len(a))]
    return sorted_a, []

# Graph algorithms
def bfs(graph, start):
    visited = set()
    order = []
    q = collections.deque([start])
    visited.add(start)
    while q:
        node = q.popleft()
        order.append(node)
        for nei in graph.get(node, []):
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
    return order

def dfs(graph, start):
    visited = set()
    order = []
    def _dfs(u):
        visited.add(u)
        order.append(u)
        for v in graph.get(u, []):
            if v not in visited:
                _dfs(v)
    _dfs(start)
    return order

def dijkstra(graph, source):
    # graph: {u: [(v, w), ...], ...}
    dist = {node: float('inf') for node in graph}
    dist[source] = 0
    heap = [(0, source)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))
    return dist

if __name__ == '__main__':
    # quick sanity check
    arr = [5,2,3,1,4]
    print("bubble:", bubble_sort(arr)[0])
    print("merge:", merge_sort(arr)[0])
    print("quick:", quick_sort(arr)[0])
    print("heap:", heap_sort(arr)[0])
    g = {1:[2,3],2:[4],3:[4],4:[]}
    print("bfs:", bfs(g,1))
    print("dfs:", dfs(g,1))