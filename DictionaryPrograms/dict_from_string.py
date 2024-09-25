'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 19:10
    @Title : Python program to create a dictionary from a string with letter count
'''

def create_dict_from_string(sample_str):
    """
    Description:
        This function creates a dictionary from a string and tracks the count of each character.
    Parameters:
        sample_str (str): The input string to create a dictionary from.
    Return:
        None
    """
    char_count = {}
    for char in sample_str:
        char_count[char] = char_count.get(char, 0) + 1
    print(f"Character count dictionary for '{sample_str}':", char_count)

def main():
    sample_str = input("Enter a string: ")
    create_dict_from_string(sample_str)

if __name__ == "__main__":
    main()
