def howMany(aDict):
    count = 0
    for i in aDict:
        count += len(aDict[i])
    print count
    return count