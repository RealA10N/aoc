from queue import Queue
from day12 import *

def bfs():
    path: PathMapType = dict()
    q: Queue[PointType] = Queue()
    q.put(end)
    while not q.empty():
        p = q.get()
        if grid[p] == 0:
            return path_length(path, end, p)
        for pt in neighbors(p):
            if pt not in path and grid[p] <= grid[pt] + 1:
                q.put(pt)
                path[pt] = p

print(bfs())
