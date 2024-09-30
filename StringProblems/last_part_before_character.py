'''
    @Author: VEMULA DILEEP
    @Date: 30-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:45
    @Title : Python program to get the last part of a string before a specified character.
'''

def last_part_before_character(s, char):
    """
    Description:
        This function returns the last part of the string before the specified character.
    Parameters:
        s : str
        char : str
    Return:
        str : substring before the specified character
    """
    return s.rsplit(char, 1)[0]

def main():
    sample_string = "https://www.w3resource.com/python-exercises"
    last_part = last_part_before_character(sample_string, "/")
    print(f"Last part before '/': {last_part}")

if __name__ == "__main__":
    main()
