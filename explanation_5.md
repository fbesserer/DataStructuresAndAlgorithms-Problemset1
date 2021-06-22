### Problem 5 Blockchain 
Time efficiency of adding a new block to the chain largely depends on the difficulty level that is chosen in the chain class. 
depending on it the calc_hash function has to loop various times in order to find a nonce value that satisfies the needs of the hash (number of "0" in the 
beginning of the hash) before it can be added to the chain. I would argue that the rest of the code can be neglected in terms of having far less of a weight on runtime. 
space complexity is that of a linkedlist and grows linearly with added blocks. 
