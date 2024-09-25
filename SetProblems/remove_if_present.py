'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 20:20
    @Title : Python program to remove an item from set if present
'''

def remove_if_present(my_set, element):
    """
    Description:
        This function removes an element if it is present in the set.
    Parameters:
        my_set (set): The set to check and remove the element
        element (any): The element to remove if present
    Return:
        set: The updated set
    """
    if element in my_set:
        my_set.remove(element)
    return my_set

def main():
    my_set = {1, 2, 3, 4, 5}
    result = remove_if_present(my_set, 3)
    print("Set after removal (if present):", result)

if __name__ == "__main__":
    main()
