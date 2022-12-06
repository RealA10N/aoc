MoveType = tuple[int,int,int]
BucketType = list[str]

def parse(text: str) -> tuple[list[BucketType], list[MoveType]]:
    a, b = [x.split('\n') for x in text.read().split('\n\n')]
    length = len(a[-1])
    n = (length // 4) + 1
    buckets = [list() for i in range(n)]

    for line in a[:-1]:
        line.ljust(length)
        for bucket, ltr in zip(buckets, line[1::4]):
            if not ltr.isspace():
                bucket.insert(0, ltr)
    
    moves = [
        tuple(
            int(x)
            for x in line.split()
            if x.isnumeric()
        )
        for line in b
        if line.strip()
    ]

    return buckets, moves
