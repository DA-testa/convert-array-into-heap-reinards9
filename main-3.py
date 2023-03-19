import sys

def build_heap(heap, n):
    swaps = []
    for i in range(n // 2, -1, -1):
        sift_down(heap, swaps, i)
    return swaps

def sift_down(heap, swaps, i):
    min_idx = i
    l = 2 * i + 1
    if l < len(heap) and heap[l] < heap[min_idx]:
        min_idx = l
    r = 2 * i + 2
    if r < len(heap) and heap[r] < heap[min_idx]:
        min_idx = r
    if i != min_idx:
        heap[i], heap[min_idx] = heap[min_idx], heap[i]
        swaps.append((i, min_idx))
        sift_down(heap, swaps, min_idx)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    assert n == len(data)
    swaps = build_heap(data, n)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)



