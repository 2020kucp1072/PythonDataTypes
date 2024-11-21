'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 20:15
    @Title : Python program to clear a set
'''

def clear_set(my_set):
    """
    Description:
        This function clears all elements from a set.
    Parameters:
        my_set : set
            The set to clear
    Return:
        None
    """
    my_set.clear()
    print("Cleared Set:", my_set)

def main():
    my_set = {1, 2, 3}
    clear_set(my_set)

if __name__ == "__main__":
    main()
