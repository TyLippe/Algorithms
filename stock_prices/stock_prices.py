#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #define max profit
  max_profit = float('-inf')
  #loop through list of profits
  for i in range(0, len(prices) - 1): 
    #loop through the profits before the current
    for j in range(0, i):
      #find difference of each index that comes before current index
      total = prices[i] - prices [j]
      if total > max_profit:
      #if the difference is higher to prior differences, reiterate max_profit
        max_profit = total
  #return max profit
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))