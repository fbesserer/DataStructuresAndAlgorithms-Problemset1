### Problem 3 Huffman Coding
the huffman tree is created using a min heap due to performance reasons. deleting elements and heapifying the tree takes O(log n) time. 
Constructing a huffman tree from a sorted array or min heap takes linear time O(n).
I have noted the time efficiency next to every function in order to make it clearer what it refers to. 
The overall runtime is quasilinear O(n log(n)) with the bottleneck being the required sorting of char - frequency in ascending order 

####space complexity 
for the char_freq_mapping(data) = 2 dicts are created for that purpose --> O(2n) 
min heap = a list (dyn array) to keep the entries, O(n) 
huffman tree is a linear data structure with n elements O(n) 
for the char mapping another dictionary is initialized O(n). In order to traverse the tree some local variables ie "string" are initialized for each recursive call --> O(n)  
the encoded data is stored in a string which takes linear space depending on the amount of chars. -> O(n) 








