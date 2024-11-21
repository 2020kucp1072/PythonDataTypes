'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:35
    @Title : Python program to list all files in a directory
'''

import os

def list_files(directory):
    """ 
    Description:
        This function lists all files in the given directory.
    Parameters:
        directory: Path of the directory
    Return:
        None
    """
    files = os.listdir(directory)
    for file in files:
        print(file)

def main():
    directory = input("Enter the directory path: ")
    list_files(directory)

if __name__ == "__main__":
    main()
