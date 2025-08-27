import time, random, statistics, os
import matplotlib.pyplot as plt
import numpy as np
from algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort, bfs, dfs, dijkstra

os.makedirs("outputs", exist_ok=True)

def time_algo(func, arr, repeat=3):
    times = []
    for _ in range(repeat):
        arr_copy = arr.copy()
        t0 = time.perf_counter()
        func(arr_copy)
        t1 = time.perf_counter()
        times.append(t1-t0)
    return statistics.mean(times)

def benchmark_sorts():
    sizes = [100, 500, 1000, 2000]
    algos = [
        ("Bubble", lambda a: bubble_sort(a)[0]),
        ("Insertion", lambda a: insertion_sort(a)[0]),
        ("Merge", lambda a: merge_sort(a)[0]),
        ("Quick", lambda a: quick_sort(a)[0]),
        ("Heap", lambda a: heap_sort(a)[0])
    ]
    results = {name: [] for name, _ in algos}
    for n in sizes:
        arr = random.sample(range(n*3), n)
        for name, fn in algos:
            t = time_algo(fn, arr, repeat=1)
            results[name].append(t)
            print(f"Size {n}, {name}: {t:.6f}s")
    # plot results
    for name in results:
        plt.figure()
        plt.plot(sizes, results[name], marker='o')
        plt.title(f"Runtime vs Input Size - {name} Sort")
        plt.xlabel("Input size (n)")
        plt.ylabel("Time (seconds)")
        plt.grid(True)
        out = os.path.join("outputs", f"{name.lower()}_benchmark.png")
        plt.savefig(out)
        print("Saved", out)
        plt.close()

def benchmark_graphs():
    # Build random weighted graphs of increasing size and run dijkstra
    node_counts = [50, 100, 200, 400]
    results = []
    for n in node_counts:
        # generate sparse random graph
        graph = {i: [] for i in range(n)}
        for u in range(n):
            for _ in range(3): # 3 edges per node on average
                v = random.randrange(n)
                w = random.randint(1, 20)
                graph[u].append((v,w))
        t0 = time.perf_counter()
        dijkstra(graph, 0)
        t1 = time.perf_counter()
        results.append(t1-t0)
        print(f"Dijkstra on {n} nodes: {t1-t0:.6f}s")
    plt.figure()
    plt.plot(node_counts, results, marker='o')
    plt.title("Dijkstra Runtime vs Nodes")
    plt.xlabel("Number of nodes")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    out = os.path.join("outputs", f"dijkstra_benchmark.png")
    plt.savefig(out)
    print("Saved", out)
    plt.close()

if __name__ == '__main__':
    benchmark_sorts()
    benchmark_graphs()