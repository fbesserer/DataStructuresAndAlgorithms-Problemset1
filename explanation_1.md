### Problem 1 LRU Cache
The point of a cache is to retrieve data that has been used recently as fast as possible. Therefore a python dictionary (hashmap) is used as storage for the cache data.
Average access time efficiency of a dictionary is O(1) 
In order to track the elements of the cache that have to be deleted once the cache is full and new data is to be added, a doubly linked list is used, where one end 
holds the most recently used data and the other end holds the least recently used data. The list ist constantly updated whenever a call of some sort is made to the cache. 
Space complexity of the storage (dictionary) is O(n). The size of the doubly linked list depends on the size of the cache and expands linearly with it which makes a total space 
complexity of O(n).

time complexity: 

LRU_cache.get(): O(1) 
 - key in self.table on average O(1) 
 - place_front O(1)

LRU_cache.delete(): O(1) ´

 - dll.pop() O(1) (popping end of linkedlist) 
 - del key from dict on average O(1)

LRU_cache.set(): O(1)
 - len() O(1)
 - key in self.table = O(1) 
 - add_node() = O(1) 

