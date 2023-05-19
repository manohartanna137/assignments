import math

def iterables(size,input,K):
    count = len(list(filter(lambda x: x == "a",input)))
    total = math.comb(size,K)
    no_a = math.comb(size-count, K)
    result = 1 - no_a/total
    print(result)
    return "{0:.3f}".format(result)