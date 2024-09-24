'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:55
    @Title : Python program to get the number of occurrences of a specified element in an array
'''

import array as arr

def count_occurrences(element):
    """
    Description:
        This function counts and returns the number of occurrences of a specified element in the array.
    Parameters:
        element (int): The element whose occurrences need to be counted.
    Return:
        None
    """
    int_array = arr.array('i', [10, 20, 30, 10, 50, 10])
    count = int_array.count(element)
    print(f"Element {element} occurs {count} times in the array.")

def main():
    element = int(input("Enter the element to count occurrences: "))
    count_occurrences(element)

if __name__ == "__main__":
    main()
