'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 20:25
    @Title : Python program to find the maximum and minimum value in a set
'''

def max_min_set(my_set):
    """
    Description:
        This function finds the maximum and minimum values in a set.
    Parameters:
        my_set : set
            The set to find the max and min from
    Return:
        None
    """
    print("Maximum Value:", max(my_set))
    print("Minimum Value:", min(my_set))

def main():
    my_set = {1, 2, 3, 4, 5}
    max_min_set(my_set)

if __name__ == "__main__":
    main()
