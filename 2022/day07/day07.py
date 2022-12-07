import collections
from typing import Union

FileType = int
DirectoryType = dict[str, Union['DirectoryType', FileType]]


def defaultdict_factory():
    return collections.defaultdict(defaultdict_factory)


def travel(d: DirectoryType, path: list[str]):
    for dir in path:
        d = d[dir]
    return d


def parse(s: str) -> DirectoryType:

    path = []
    files: DirectoryType = defaultdict_factory()

    for line in s.split('\n'):
        tokens = line.split()
        if not tokens:
            continue

        if tokens[0] == '$':
            if tokens[1] == 'cd':
                if tokens[2] == '/':
                    path.clear()
                if tokens[2] == '..':
                    path.pop()
                else:
                    path.append(tokens[2])

        elif tokens[0].isnumeric():
            travel(files, path)[tokens[1]] = int(tokens[0])

    return files
