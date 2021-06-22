###Problem 6 Union and Intersection 
Both union and intersection functions require a complete loop of both linked lists in order to get the values and compare them. Time complexity for the loop operation is 
therefore O(n + m) with n and m being the nodes of either linked list respectively. 
For the newly created union or intersection linked list new nodes can be appended in constant time.
The only other data structure used to compare values of the input data is a set which has constant adding and removal features. 
Therefore overall time complexity is linear O(n). 