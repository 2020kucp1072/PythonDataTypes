'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:30
    @Title : Python program to add a key to a dictionary
'''

def add_key_to_dict():
    """
    Description:
        This function adds a key-value pair to an existing dictionary.
    Parameters:
        None
    Return:
        None
    """
    sample_dict = {0: 10, 1: 20}
    sample_dict[2] = 30
    print("Updated dictionary:", sample_dict)

def main():
    add_key_to_dict()

if __name__ == "__main__":
    main()
