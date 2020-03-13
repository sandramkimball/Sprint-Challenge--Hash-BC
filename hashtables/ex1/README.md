# Merging Two Packages

Given a package with a weight limit `limit` and a list `weights` of item weights, implement a function `get_indices_of_item_weights` that finds two items whose sum of weights equals the weight limit `limit`. Your function will return an instance of an `Answer` tuple that has the following form:

    (zero, one) OR [zero, one]???

where each element represents the item weights of the two packages. _**The higher valued index should be placed in the `zeroth` index and the smaller index should be placed in the `first` index.**_ If such a pair doesn’t exist for the given inputs, your function should return `None`.

Your solution should run in linear time.

Example:
```
input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
output: [ 3, 1 ]  # since these are the indices of weights 15 + 6 = 21

get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21)
returns [3, 1] = 21
```

## ToDo
 
* Build two nested loops, yielding a quadratic-runtime solution. 

* Use a hash table to implement a solution with better runtime.

* Store  ____ in the hash table to solve the problem efficiently. 

* Store `key`:`weight` in the input list. 

* Store `value`:`weight[index]`.

* Check if ht contains an entry for `limit - weight`. If  so, we've found the two items whose weights sum up to the `limit`/

* If not, return `None`

* .sort()


1) Explain 3 heigh-level array fncs work down to memory level.
2) Tests pass, solution uses hash table (+collirion handle and resizing)
3) Diagrame, code blockchain using crypto hash
4) Proof of Work in blockchain - mine a coin before lunch.
4) Protocol for nodes in blockchain ntwrk to communicate