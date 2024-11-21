'''
    @Author: VEMULA DILEEP
    @Date: 26-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:50
    @Title : Python program to convert a list to a tuple
'''

def list_to_tuple(lst):
    """
    Description:
        This function converts a list to a tuple.
    Parameters:
        lst : list
    Return:
        tuple : converted tuple from the list
    """
    return tuple(lst)

def main():
    lst = [1, 2, 3, 4, 5]
    result = list_to_tuple(lst)
    print("Converted Tuple:", result)

if __name__ == "__main__":
    main()
