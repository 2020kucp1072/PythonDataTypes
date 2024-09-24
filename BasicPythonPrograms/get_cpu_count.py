'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:30
    @Title : Python program to find out the number of CPUs used
'''

import os

def get_cpu_count():
    """ 
    Description:
        This function returns the number of CPUs used.
    Parameters:
        None
    Return:
        None
    """
    print(f"Number of CPUs available: {os.cpu_count()}")

def main():
    get_cpu_count()

if __name__ == "__main__":
    main()
