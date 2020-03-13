#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16) #(self, capacity)
    total_weight = 0
    answer = ()
    hash_table_insert(ht, 21, weights[0]) #(hashtable, key, value)

    while i < len(weights) + 1:
       if weights[i] + hash_table_retrieve(ht, i[0]) < hash_table_retrieve(ht, i):
           answer = (hash_table_retrieve(ht, i), weights[i])
           
        else:
            return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
