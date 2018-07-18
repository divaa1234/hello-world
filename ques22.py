def biggest(aDict):
    biggest = 0
    collection = []
    if len(aDict) == 0:
        return None
    for e in aDict:
        if len(aDict[e]) >= biggest:
            biggest = len(aDict[e])
            collection = e
    return str(collection)