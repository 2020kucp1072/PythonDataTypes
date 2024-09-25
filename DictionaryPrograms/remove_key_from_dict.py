'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:50
    @Title : Python program to remove a key from a dictionary
'''

def remove_key_from_dict(key_to_remove):
    """
    Description:
        This function removes the specified key from the dictionary.
    Parameters:
        key_to_remove (int): The key to be removed.
    Return:
        None
    """
    sample_dict = {0: 10, 1: 20, 2: 30}
    if key_to_remove in sample_dict:
        del sample_dict[key_to_remove]
        print(f"Dictionary after removing key {key_to_remove}:", sample_dict)
    else:
        print(f"Key {key_to_remove} not found in the dictionary.")

def main():
    key_to_remove = int(input("Enter the key to remove: "))
    remove_key_from_dict(key_to_remove)

if __name__ == "__main__":
    main()
