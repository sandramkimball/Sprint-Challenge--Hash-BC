#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def insert(self, index, value): #index = location, place, address
    #first, check if: is there open space/index in range, shift things right, insert

    if self.count >= self.capacity:
        self.double_size()

    if index > self.count: #extra space gaps cause problemos
        print ('err: out of range')
        return
    
    #start with last, move right, iterate backwards:
    for i in range(self.count, index, -1):
        self.storage[i] = self.storage[i-1]

    self.storage[index] = value
    self.count += 1

def append(self, value):
    self.insert(self.count, value)

def reconstruct_trip(tickets, length): # O(1) linear time
    hashtable = HashTable(length)
    route = [None] * length # self.storage

    hash(key=source, value=destination)

    while i < len(tickets) + 1:
        if i[key] == i + 1[value]:
            hash_table_insert(i, i+1)
            i += 1
        else: 
            i += 1

        # origin - insert to front - (self, index, value)
        if i[key] == 'NONE':
            self.insert(0, i[value])
            
        # final destination - append to end - (self, value)
        if i[value] == 'NONE':
           self.append(i[key]) 
    
    return route
