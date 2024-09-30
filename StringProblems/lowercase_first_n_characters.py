'''
    @Author: VEMULA DILEEP
    @Date: 30-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:05
    @Title : Python program to lowercase first n characters in a string.
'''

def lowercase_first_n(s, n):
    """
    Description:
        This function lowercases the first n characters of the string.
    Parameters:
        s : str
        n : int
    Return:
        str : modified string
    """
    return s[:n].lower() + s[n:]

def main():
    sample_string = "HELLO WORLD"
    n = 5
    modified_string = lowercase_first_n(sample_string, n)
    print(f"Modified string: {modified_string}")

if __name__ == "__main__":
    main()
