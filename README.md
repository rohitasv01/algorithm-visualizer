# Algorithm Visualizer & Benchmarking Tool

**Resume-ready project:** Implements classic sorting and graph algorithms, provides benchmarking scripts and simple visualizations. Good to demonstrate DSA skills, benchmarking understanding, and basic data visualization.

## Features
- Implementations: Bubble, Insertion, Merge, Quick, Heap sorts
- Graph algorithms: BFS, DFS, Dijkstra
- Benchmarking: runtime vs input size plots (saved to `outputs/`)
- Visualization: sorting animation generator (saves GIF using ImageMagick/Matplotlib)

## Requirements
Python 3.8+
```
pip install -r requirements.txt
```

## Quick start
1. Run benchmarks and produce PNGs:
```
python benchmark.py
```
2. Create a sorting animation (requires ImageMagick to be installed on the system):
```
python visualize_sort.py
```

## Resume description (copy-paste)
**Algorithm Visualizer & Benchmarking Tool** (Python, Matplotlib, NumPy)  
- Implemented sorting algorithms (QuickSort, MergeSort, HeapSort, Insertion, Bubble) and graph algorithms (BFS, DFS, Dijkstra).  
- Benchmarked runtimes across input sizes and plotted performance curves.  
- Built a visualization module to animate sorting steps (saved as GIF).  
- Repo: `github.com/rohitasv01/algorithm-visualizer`

## Files of interest
- `algorithms.py` – implementations of algorithms
- `benchmark.py` – benchmarking scripts that save PNG plots to `outputs/`
- `visualize_sort.py` – creates a GIF of sorting steps (requires ImageMagick)