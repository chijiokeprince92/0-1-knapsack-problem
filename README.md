This problem is under the module "AI for Search and Optimization" This repository displays the code for solving the 0-1 Knapsack problem.

The knapsack problem is the following problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine which items to include in the collection The collection should be that the total weight is less than or equal to a given limit and the total value is as large as possible.

The 0-1 knapsack problem is slightly different from the knapsack problem in that in the former, each identical item has the chance to be picked just once So if you have two laptops in your collection, you're expected to pick just one in your final solution.

This code uses a bruteforce approach to find the best set with the highest value, by permutating over all possible outcomes. Note: The time complexity of the bruteforce approach increases as the number of items increase.