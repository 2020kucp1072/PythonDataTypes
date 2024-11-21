'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 19:35
    @Title : Python program to count number of items in a dictionary value that is a list
'''

def count_list_items_in_dict(sample_dict):
    """
    Description:
        This function counts the number of items in dictionary values that are lists.
    Parameters:
        sample_dict (dict): The dictionary with list values.
    Return:
        None
    """
    for key, value in sample_dict.items():
        if isinstance(value, list):
            print(f"Key '{key}' has {len(value)} items.")

def main():
    sample_dict = {'A': [1, 2, 3], 'B': [4, 5], 'C': 'Not a list'}
    count_list_items_in_dict(sample_dict)

if __name__ == "__main__":
    main()
