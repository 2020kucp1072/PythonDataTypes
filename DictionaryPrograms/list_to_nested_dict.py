'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 19:25
    @Title : Python program to convert a list into a nested dictionary of keys
'''

def list_to_nested_dict(lst):
    """
    Description:
        This function converts a list into a nested dictionary.
    Parameters:
        lst (list): The input list to convert.
    Return:
        None
    """
    nested_dict = current = {}
    for item in lst:
        current[item] = {}
        current = current[item]
    print("Nested dictionary:", nested_dict)

def main():
    lst = ['A', 'B', 'C', 'D']
    list_to_nested_dict(lst)

if __name__ == "__main__":
    main()
