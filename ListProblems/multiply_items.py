'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Title : Python program to multiply all the items in a list
'''

from functools import reduce

def multiply_list(items):
    """
    Description:
        This function returns the product of all items in a list.
    Parameters:
        items : list of numbers
    Return:
        int : product of all items
    """
    return reduce(lambda x, y: x * y, items)

def main():
    sample_list = [1, 2, 3, 4, 5]
    result = multiply_list(sample_list)
    print("Product:", result)

if __name__ == "__main__":
    main()
