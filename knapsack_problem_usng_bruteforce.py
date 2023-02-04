#import pandas
import pandas as pd

#read the csv file using pandas and handle exception
try: 
    knapsack = pd.read_csv('problem_b.csv')
    #extract the columns containing the items, weight, and value into variables
    items = knapsack['item']
    weight = knapsack['weight']
    value = knapsack['value']

    # Create a variable to represent the knapsack capacity
    bagCapacity = 2000

    # Get the length of the items
    len_of_items = len(items)

    # Create an empty array that represents the collection of items that has the highest value and not exceeding the knapsack capacity
    packedItem = []


    def knapsack(items, max_weight):
        # items or max weight is 0
        if not items or max_weight == 0:
            return 0
        
        # Recursive case: try both including and excluding the current item
        value, weight = items[0]
        if weight > max_weight:
            return knapsack(items[1:], max_weight)
        else:
            return max(knapsack(items[1:], max_weight), knapsack(items[1:], max_weight-weight) + value)

    # Example input
    items = [(60, 10), (100, 20), (120, 30)]
    max_weight = 50

    print(knapsack(items, max_weight))

except Exception:
    print('File does not exist')

#This code defines a knapsack function that uses recursion to try all possible combinations of items.
# The base case is when there are no items or the maximum weight is 0, in which case the function returns 0. 
# The recursive case considers two options: including the current item or excluding it. 
# If the weight of the current item is greater than the maximum weight, the item must be excluded. 
# Otherwise, the function tries both options and returns the maximum value.

#Note that this algorithm has a time complexity of O(2^n), where n is the number of items, so it may be slow for large inputs.