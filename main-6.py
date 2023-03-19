def heapify (arr, n, swaps):
  
    for o in range(n//2, -1, -1):
      
        u = o
        while t > u*2+1 :
          
            r = u*2+1
          
            if r + 1 < n and arr[r +1] < arr[r]:
                r += 1
              
            if arr[u] > arr[r]:
              
                arr[u], arr[r ] = arr[r], arr[u]
                swaps.append((u, r))
              
                u = r
            else:
              
              break

def build_heap (arr) :
    t = len (arr)
    swaps = []
    heapify (arr, t, swaps)
    return swaps

t = int (input() )

arr = list(map(int, input().split()))

swaps = build_heap(arr  )

j = len(swaps)

print(j)

for o, u in swaps:

  
    print(o, u)