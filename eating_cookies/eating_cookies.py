#!/usr/bin/python

import sys

#add cache to shorten runtime
cache = {0:1, 1:1, 2:2, 5:13}
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=cache):
    # base case
    if n == 0 or n == 1: 
        return 1
    # if n is in the cache already, return the value
    elif n in cache:
        return cache[n]
    #if not we will add it to cache
    else:
        # I did three based off three cookies most at once. 
        #recursively call our function, until we find 3 values that are already cached, while caching those. Trippy 
        cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    return cache[n]
    

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')