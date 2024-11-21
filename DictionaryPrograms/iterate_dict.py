'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:40
    @Title : Python program to iterate over a dictionary using for loops
'''

def iterate_dict():
    """
    Description:
        This function iterates over a dictionary and prints key-value pairs.
    Parameters:
        None
    Return:
        None
    """
    sample_dict = {'A': 1, 'B': 2, 'C': 3}
    
    for key, value in sample_dict.items():
        print(f"Key: {key}, Value: {value}")

def main():
    iterate_dict()

if __name__ == "__main__":
    main()
