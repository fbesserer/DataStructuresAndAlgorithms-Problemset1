'''
Active Directory

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such.
Where User is represented by str representing their ids.

Write a function that provides an efficient look up of whether the user is in a group.
'''
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = list()
        self.users = set()

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.add(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    if group.groups:  # if subgroups exist
        if user in group.users:
            return True
        for subgroup in group.groups:
            return is_user_in_group(user, subgroup)
    if user in group.users:
        return True
    return False

#  Testcase 1
print("----- Testcase Nr 1 -----")
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
not_existing_user = "not_exist"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(sub_child_user, parent))  # True
print(is_user_in_group(not_existing_user, parent))  # False
print(is_user_in_group(sub_child_user, child))  # True
print(is_user_in_group(not_existing_user, child))  # False
print(is_user_in_group(sub_child_user, sub_child))  # True
print(is_user_in_group(not_existing_user, sub_child))  # False

print("----- Testcase Nr 2 -----")

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

parent_user = "parent_user"
parent.add_user(parent_user)

child.add_group(sub_child)
parent.add_group(child)

print(is_user_in_group(parent_user, parent))  # True
print(is_user_in_group(parent_user, child))  # False
print(is_user_in_group(parent_user, sub_child))  # False

print("----- Testcase Nr 3 -----")

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")
sub_child1 = Group("subchild")
sub_child2 = Group("subchild")
sub_child3 = Group("subchild")

sub_child_user = "sub_child_user"
not_existing_user = "not_exist"
sub_child3.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
sub_child.add_group(sub_child1)
sub_child1.add_group(sub_child2)
sub_child2.add_group(sub_child3)

print(is_user_in_group(not_existing_user, parent))  # False
print(is_user_in_group(not_existing_user, child))  # False
print(is_user_in_group(not_existing_user, sub_child3))  # False
print(is_user_in_group(sub_child_user, parent))  # True
print(is_user_in_group(sub_child_user, child))  # True
print(is_user_in_group(sub_child_user, sub_child))  # True
print(is_user_in_group(sub_child_user, sub_child1))  # True
print(is_user_in_group(sub_child_user, sub_child2))  # True
print(is_user_in_group(sub_child_user, sub_child3))  # True
