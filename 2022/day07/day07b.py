from day07 import parse, DirectoryType
from math import inf

with open('input', 'r') as file:
    files = parse(file.read())


def dfs(dir: DirectoryType | int) -> int:
    if isinstance(dir, int):
        return dir
    return sum(dfs(x) for x in dir.values())


AVAILABLE = 70000000
NEEDED = 30000000
unused = AVAILABLE - dfs(files)
TO_FREE = NEEDED - unused
smallest = inf


def dfs2(dir: DirectoryType) -> int:
    global smallest
    if isinstance(dir, int):
        return dir
    sz = sum(dfs2(x) for x in dir.values())
    if TO_FREE <= sz <= smallest:
        smallest = sz
    return sz


dfs2(files)
print(smallest)
