### Problem 2 File Recursion
Since we are trying to find all the files with a given suffix it is by definition necessary to loop through all files and folders of a given path. 
I chose a recursive approach that performs a pre order depth first search and has a time complexity of O(n) since every file or folder is visited exactly once. 
Space complexity is also at most linear with O(n) with n files and folders. 



