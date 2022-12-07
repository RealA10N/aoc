from day07 import parse, DirectoryType

with open('input', 'r') as file:
    files = parse(file.read())

size = 0
THRESHOLD = 100000


def dfs(dir: DirectoryType | int) -> int:
    global size
    if isinstance(dir, int):
        return dir
    sz = sum(dfs(x) for x in dir.values())
    if sz <= THRESHOLD:
        size += sz
    return sz


dfs(files)
print(size)
