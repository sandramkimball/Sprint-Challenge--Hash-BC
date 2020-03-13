#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable, #(self, capacity)
                        hash_table_insert, #(hash_table, key, value)
                        hash_table_remove, #(hash_table, key)
                        hash_table_retrieve) #(hash_table, key)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16) 
    # total_weight = 0
    # answer = ()
    # pair = ()
    # i = 0
    
    for i in range(length): # O(n)
        difference = limit - weights[i]
        value = hash_table_retrieve(ht, difference)

        if value is not None:
            pair = (value, weights[i])

            if value < weights[i]:
                pair = (weights[i], value)

            return pair

        hash_table_insert(ht, weights[i], i)

    return None

    # for weight in weights:
    #     value = hash_table_retrieve(ht, limit - weight)
    #     Index = weights[weight]

    #     if value:
    #         return value, Index
        
    # return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
