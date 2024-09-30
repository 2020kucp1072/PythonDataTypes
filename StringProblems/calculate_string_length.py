'''
    @Author: VEMULA DILEEP
    @Date: 30-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:10
    @Title : Python program to calculate the length of a string.
'''

def calculate_length(s):
    """
    Description:
        This function calculates the length of a given string.
    Parameters:
        s : str
    Return:
        int : length of the string
    """
    return len(s)

def main():
    sample_string = "Hello, World!"
    length = calculate_length(sample_string)
    print(f"Length of the string: {length}")

if __name__ == "__main__":
    main()
