'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 19:30
    @Title : Python program to check if multiple keys exist in a dictionary
'''

def check_keys_in_dict(sample_dict, keys):
    """
    Description:
        This function checks if all the specified keys exist in the dictionary.
    Parameters:
        sample_dict (dict): The dictionary to check.
        keys (list): The list of keys to check in the dictionary.
    Return:
        None
    """
    if all(key in sample_dict for key in keys):
        print(f"All keys {keys} exist in the dictionary.")
    else:
        print(f"Not all keys {keys} exist in the dictionary.")

def main():
    sample_dict = {'A': 1, 'B': 2, 'C': 3}
    keys_to_check = ['A', 'C']
    check_keys_in_dict(sample_dict, keys_to_check)

if __name__ == "__main__":
    main()
