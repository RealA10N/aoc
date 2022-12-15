from queue import Queue
from day12 import *

def bfs():
    path: PathMapType = dict()
    q: Queue[PointType] = Queue()
    q.put(start)
    while not q.empty():
        p = q.get()
        if p == end:
            return path_length(path, start, end)
        for pt in neighbors(p):
            if pt not in path and grid[pt] <= grid[p] + 1:
                q.put(pt)
                path[pt] = p

print(bfs())
