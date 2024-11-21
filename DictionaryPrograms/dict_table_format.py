'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 19:15
    @Title : Python program to print a dictionary in table format
'''

def print_dict_table_format(sample_dict):
    """
    Description:
        This function prints the dictionary in a table format with keys and values.
    Parameters:
        sample_dict (dict): The dictionary to be printed in table format.
    Return:
        None
    """
    print("{:<10} {:<10}".format('Key', 'Value'))
    for key, value in sample_dict.items():
        print("{:<10} {:<15}".format(key, value))

def main():
    sample_dict = {1: 'One', 2: 'Two', 3: 'Three'}
    print_dict_table_format(sample_dict)

if __name__ == "__main__":
    main()
