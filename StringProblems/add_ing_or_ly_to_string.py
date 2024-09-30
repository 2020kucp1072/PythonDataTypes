'''
    @Author: VEMULA DILEEP
    @Date: 30-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:25
    @Title : Python program to add 'ing' at the end of a given string.
'''

def add_ing(s):
    """
    Description:
        This function adds 'ing' to the end of a string, or 'ly' if it already ends with 'ing'.
    Parameters:
        s : str
    Return:
        str : modified string
    """
    if len(s) < 3:
        return s
    if s.endswith("ing"):
        return s + "ly"
    return s + "ing"

def main():
    sample_string1 = "abc"
    sample_string2 = "string"
    result1 = add_ing(sample_string1)
    result2 = add_ing(sample_string2)
    print(f"Modified string 1: {result1}")
    print(f"Modified string 2: {result2}")

if __name__ == "__main__":
    main()
