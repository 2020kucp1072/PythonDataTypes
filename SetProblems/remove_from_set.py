'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 20:15
    @Title : Python program to remove item(s) from set
'''

def remove_from_set(my_set, element):
    """
    Description:
        This function removes a specific element from the set.
    Parameters:
        my_set (set): The set to remove the element from
        element (any): The element to be removed
    Return:
        set: The updated set
    """
    my_set.discard(element)
    return my_set

def main():
    my_set = {1, 2, 3, 4, 5}
    result = remove_from_set(my_set, 3)
    print("Set after removal:", result)

if __name__ == "__main__":
    main()
