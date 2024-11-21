'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:45
    @Title : Python program to create an array of 5 integers and display the array items by accessing individual element through indexes
'''

import array as arr

def display_array_elements():
    """
    Description:
        This function creates an array of 5 integers and prints each item individually using indexes.
    Parameters:
        None
    Return:
        None
    """
    int_array = arr.array('i', [10, 20, 30, 40, 50])
    print("Array elements accessed through indexes:")
    for i in range(len(int_array)):
        print(f"Element at index {i}: {int_array[i]}")

def main():
    display_array_elements()

if __name__ == "__main__":
    main()
