'''
Finding Files

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"
Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().
'''

import os


def find_files(suffix, path):
    paths = list()

    def rec_find_files(suffix, path):
        folders = [os.path.join(path, subpath) for subpath in os.listdir(path)]
        files = list()
        for entry in folders:
            if os.path.isdir(entry):
                files += rec_find_files(suffix, entry)
            elif str(entry).endswith(suffix):
                files.append(entry)

        return files

    if os.path.isdir(path):  # check if path is a valid path, if not return empty list
        paths = rec_find_files(suffix, path)

    return paths


test_path1 = "./testdir/"
test_path2 = "./"
test_path3 = ""

print("----- Testcase Nr 1 -----")
print(find_files(".c", test_path1))  # ['./testdir/subdir1\\a.c', './testdir/subdir1\\b.c', './testdir/subdir1\\c.c', './testdir/subdir3\\subsubdir1\\b.c', './testdir/subdir5\\a.c', './testdir/t1.c']

print("----- Testcase Nr 2 -----")
print(find_files(".py", test_path2))  # ['./problem_1_LRU_Cache.py', './Problem 1 - LRU Cache_test.py', './problem_2_file_recursion.py'] at the time of writing the program

print("----- Testcase Nr 3 -----")
print(find_files(".py", test_path3))  # empty list