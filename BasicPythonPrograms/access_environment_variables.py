'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:40
    @Title : Python program to access environment variables
'''

import os

def access_environment_variables():
    """ 
    Description:
        This function accesses and prints environment variables.
    Parameters:
        None
    Return:
        None
    """
    for key, value in os.environ.items():
        print(f"{key}: {value}")

def main():
    access_environment_variables()

if __name__ == "__main__":
    main()
