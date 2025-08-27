import matplotlib.pyplot as plt
import matplotlib.animation as animation
from algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort, heap_sort
import random, os

os.makedirs("outputs", exist_ok=True)

def animate_sort(algorithm_fn, arr, outname):
    # algorithm_fn should return (sorted_arr, steps)
    sorted_arr, steps = algorithm_fn(arr)
    if not steps:
        # fallback: show original and sorted
        steps = [arr.copy(), sorted_arr.copy()]
    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(len(arr)), steps[0])
    ax.set_title("Sorting Visualization")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr)+1)

    def update(frame):
        for rect, val in zip(bar_rects, steps[frame]):
            rect.set_height(val)
        return bar_rects

    ani = animation.FuncAnimation(fig, update, frames=len(steps), blit=False, repeat=False)
    ani.save(outname, writer='imagemagick', fps=4)
    plt.close()
    print("Saved animation to", outname)

if __name__ == '__main__':
    arr = random.sample(range(1, 30), 20)
    animate_sort(bubble_sort, arr, "outputs/bubble_sort.gif")