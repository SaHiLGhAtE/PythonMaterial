import time
from functools import lru_cache

@lru_cache(maxsize=5)
def some_work(n):
    #some work taking n seconds
    time.sleep(n)
    return n

if __name__=='__main__':
    print("Now Running some work")
    some_work(3)
    print("Done... Calling again")
    input()
    some_work(3)
    print("Called again")

