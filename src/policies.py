file = open("input.txt")
firstLine = file.readline().split(" ")

k = int(firstLine[0])
m = int(firstLine[1])

requests = [int(request) for request in file.readline().split()]

def FIFO():
    from collections import deque
    cache = {}
    queue = deque()

    numOfMisses = 0

    for request in requests:
        if request in cache:
            continue
        else:
            numOfMisses += 1
            if len(cache) == k:
                oldest = queue.popleft()
                del cache[oldest]
            cache[request] = True
            queue.append(request)
    
    print(f"FIFO : {numOfMisses}")

def LRU():
    from collections import OrderedDict
    cache = OrderedDict()

    numOfMisses = 0

    for request in requests:
        if request in cache:
            cache.move_to_end(request)
        else:
            numOfMisses += 1
            if len(cache) == k:
                cache.popitem(last=False)
            cache[request] = True

    print(f"LRU : {numOfMisses}")

def OPTFF():
    from collections import deque
    cache = {}
    order = deque() # I'm gonna use FIFO in the case of a tiebreaker

    numOfMisses = 0

    for i, request in enumerate(requests):
        if request in cache:
            continue
        else:
            numOfMisses += 1
            if len(cache) == k:
                nextAccesses = {}
                for item in cache:
                    try:
                        nextAccesses[item] = requests[i+1:].index(item)
                    except:
                        nextAccesses[item] = float('inf')
                furthestAccess = max(nextAccesses.values())
                candidates = [item for item in nextAccesses if nextAccesses[item] == furthestAccess]
                if len(candidates) == 1:
                    evict = candidates[0]
                else:
                    for item in order:
                        if item in candidates:
                            evict = item
                            break
                del cache[evict]
                order.remove(evict)

            cache[request] = True
            order.append(request)
    
    print(f"OPTFF : {numOfMisses}")

FIFO()
LRU()
OPTFF()