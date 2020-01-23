#!/usr/bin/python

import sys
    
def rock_paper_scissors(n):
  #create a list for rps
  rps = ['rock', 'paper', 'scissors']
  #blank list to hold possible plays
  poss = []
  #base case
  if n <= 0:
    return [[]]
  #build a helper function that will use recursion
  def round(left, results):
    #base case
    if left == 0:
      #add data to poss
      poss.append(results)
      return poss
    else:
      #loop through list
      for i in range(0, len(rps)):
        #recursion  time, subtract one more round, send each rps[i]
        round(left-1, results + [rps[i]])
  #call out helper function
  round(n, [])
  #return list
  return poss


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')