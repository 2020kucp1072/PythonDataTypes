'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 20:10
    @Title : Python program to add member(s) in a set
'''

def add_to_set(my_set, new_elements):
    """
    Description:
        This function adds new elements to the set.
    Parameters:
        my_set (set): The set to add elements to
        new_elements (iterable): Elements to add to the set
    Return:
        set: The updated set
    """
    my_set.update(new_elements)
    return my_set

def main():
    my_set = {1, 2, 3}
    new_elements = [4, 5]
    result = add_to_set(my_set, new_elements)
    print("Updated Set:", result)

if __name__ == "__main__":
    main()
