'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:00
    @Title : Python program to remove the first occurrence of a specified element from an array
'''

import array as arr

def remove_first_occurrence(element):
    """
    Description:
        This function removes the first occurrence of a specified element from the array.
    Parameters:
        element (int): The element whose first occurrence needs to be removed.
    Return:
        None
    """
    int_array = arr.array('i', [10, 20, 30, 10, 50])
    print("Original array:", int_array)
    
    try:
        int_array.remove(element)
        print(f"Array after removing the first occurrence of {element}:", int_array)
    except ValueError:
        print(f"Element {element} not found in the array.")

def main():
    element = int(input("Enter the element to remove its first occurrence: "))
    remove_first_occurrence(element)

if __name__ == "__main__":
    main()
