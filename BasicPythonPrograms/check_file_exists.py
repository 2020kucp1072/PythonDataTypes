'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:20
    @Title : Python program to check if a file exists
'''

import os

def check_file_exists(file_name):
    """ 
    Description:
        This function checks if a file exists in the current directory.
    Parameters:
        file_name: Name of the file to check
    Return:
        None
    """
    if os.path.exists(file_name):
        print(f"The file {file_name} exists.")
    else:
        print(f"The file {file_name} does not exist.")

def main():
    file_name = input("Enter the file name to check: ")
    check_file_exists(file_name)

if __name__ == "__main__":
    main()
