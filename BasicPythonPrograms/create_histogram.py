'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:05
    @Title : Python program to create a histogram from a given list of integers
'''

def create_histogram(items):
    """ 
    Description:
        This function creates a histogram from a given list of integers.
    Parameters:
        items: List of integers
    Return:
        None
    """
    for n in items:
        print('*' * n)

def main():
    items = [4, 6, 2, 7, 5]
    create_histogram(items)

if __name__ == "__main__":
    main()
