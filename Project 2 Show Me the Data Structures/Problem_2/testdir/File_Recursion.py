
import os

def find_files(suffix, path,output_list):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    if os.path.exists(path):
        
        if not os.path.isfile(path):
            path_list = os.listdir(path)
           
            for pathitem in path_list:
               
                if not os.path.isfile(pathitem):
                    newpath = os.path.join(path,pathitem)
                    find_files(suffix,newpath,output_list)
                if pathitem.endswith(suffix):
                    output_list.append(pathitem) 
                
    return output_list


def test_function(work_directory,suffix, solution):
    """
    test function takes work_directory,suffix, solution as input and gives the test result as pass or fail
    by comparing find_files output with expected output
    This program is assumed to be in the testdir provided in the problem statement, so the solution is compared
    with the results when current directory is testdir.
    """
    if find_files(suffix,work_directory,list()) == solution:
        print("Passed for suffix: ", suffix)
    else:
        print("Fail")
    
    return

current_work_directory = os.getcwd()
# Test Case 1
test_function(current_work_directory,".h", ['b.h', 'a.h', 't1.h', 'a.h'])

# Test Case 2
test_function(current_work_directory,".c", ['b.c', 't1.c', 'a.c', 'a.c'])

# Test Case 3
# Returns empty list if no file ends with given suffix
test_function(current_work_directory,".x", [])

# Test Case 4
# On passing null string the function gets all files, folders and subfolders in the current working directory
all_files_folders = ['.DS_Store','.gitkeep','subdir4','b.h','b.c','subsubdir1','subdir3','t1.c','.gitkeep',
                     'subdir2','a.h','a.c','subdir5','File Recursion.ipynb','dsc.tar.gz','t1.h','a.h','a.c',
                     'subdir1','File Recursion-checkpoint.ipynb','.ipynb_checkpoints','File_Recursion.py']



test_function(current_work_directory,"", all_files_folders)

# General testing of find_files
output = find_files(".c",current_work_directory,list())


