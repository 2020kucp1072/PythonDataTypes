'''
    @Author: VEMULA DILEEP
    @Date: 26-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:55
    @Title : Python program to remove an item from a tuple
'''

def remove_item(t, item):
    """
    Description:
        This function removes an item from a tuple.
    Parameters:
        t : tuple
        item : item to be removed
    Return:
        tuple : new tuple with the item removed
    """
    return tuple(x for x in t if x != item)

def main():
    t = (1, 2, 3, 4, 2, 5)
    item_to_remove = 2
    result = remove_item(t, item_to_remove)
    print("Tuple after removal:", result)

if __name__ == "__main__":
    main()
