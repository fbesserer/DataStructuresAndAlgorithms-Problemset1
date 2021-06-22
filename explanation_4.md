### Problem 4 Active Directory
I assumed that if a user is a member of a child group it is also a user of that childs parent group even if it is not directly listed as such. 
Comparable to a employee who is a member of a team, a department, a domain and of course the company itself but hierarchically stored under the team. 
My design tries to find a middle way between major space usage and excessive access time.
In the worst case scenario where there are n groups, all nested inside each other from parent to sub child and 
the most inner group has m entries, access time efficiency would be O(n), because all groups would have to be looped through
 in order to look for a specific user. 

However space efficiency in this case would also be linear with O(n) (or more precise O(n + m) which is still linear). 
Constant access time could be achieved by copying all the values of each subgroup into the group a level higher etc until reaching the parent group.
In this case time efficiency for access would be constant O(1) but space efficiency would be quadratic O(n * m). 
The above assumes average case access of set elements (O(1)). 

