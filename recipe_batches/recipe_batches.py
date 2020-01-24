#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  #define amount that can be made
  amount = float('inf')
  #check if we have the right ingredients or enough, if not return 0
  for i, j in recipe.items():
    if not i in ingredients.keys() or ingredients[i] - j < 0:
      return 0
  #loop over dict to compare recipe to ingredient 
  for i, j in recipe.items():
    #create a temp storage to compare to amount
    temp = 0
    #math how many times our ingredients can be used
    temp = ingredients[i] // j
    if temp < amount:
        #if temp is less than keep that temp number
        amount = temp
  #return the amount 
  return amount


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))