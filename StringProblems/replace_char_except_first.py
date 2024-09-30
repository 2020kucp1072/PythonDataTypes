'''
    @Author: VEMULA DILEEP
    @Date: 30-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:20
    @Title : Python program to change all occurrences of its first char to '$'.
'''

def replace_first_char(s):
    """
    Description:
        This function replaces all occurrences of the first character with '$', except the first character itself.
    Parameters:
        s : str
    Return:
        str : modified string
    """
    first_char = s[0]
    return first_char + s[1:].replace(first_char, '$')

def main():
    sample_string = "restart"
    modified_string = replace_first_char(sample_string)
    print(f"Modified string: {modified_string}")

if __name__ == "__main__":
    main()
