'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:50
    @Title : Python program to reverse the order of items in the array
'''

import array as arr

def reverse_array():
    """
    Description:
        This function reverses the order of items in the array and prints it.
    Parameters:
        None
    Return:
        None
    """
    int_array = arr.array('i', [10, 20, 30, 40, 50])
    print("Original array:", int_array)
    int_array.reverse()
    print("Reversed array:", int_array)

def main():
    reverse_array()

if __name__ == "__main__":
    main()
