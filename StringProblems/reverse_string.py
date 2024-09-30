'''
    @Author: VEMULA DILEEP
    @Date: 30-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:00
    @Title : Python program to reverse a string.
'''

def reverse_string(s):
    """
    Description:
        This function reverses the given string.
    Parameters:
        s : str
    Return:
        str : reversed string
    """
    return s[::-1]

def main():
    sample_string = "Hello, World!"
    reversed_str = reverse_string(sample_string)
    print(f"Reversed string: {reversed_str}")

if __name__ == "__main__":
    main()
