#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable, #(self, capacity)
                        hash_table_insert, #(hash_table, key, value)
                        hash_table_remove, #(hash_table, key)
                        hash_table_retrieve) #(hash_table, key)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16) 
    total_weight = 0
    answer = ()
    i = 0
    hash_table_insert(ht, 21, weights[0]) 

    difference = limit - weights[i]
    target = hash_table_retrieve(ht, difference)

    for i in range(length):
        if weights[i] + weights[i+1] < limit:
            hash_table_insert(ht, key=weights[i], value=i)
            
            i += 1
            return 
        
        if target is not None:
            return (i, target)
            hash_table_insert(ht, weights[i], i)

        else:
            return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
