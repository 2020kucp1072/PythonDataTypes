'''
    @Author: VEMULA DILEEP
    @Date: 30-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:55
    @Title : Python program to count occurrences of a substring in a string.
'''

def count_substring(s, substring):
    """
    Description:
        This function counts the occurrences of a substring in the string.
    Parameters:
        s : str
        substring : str
    Return:
        int : count of occurrences
    """
    return s.count(substring)

def main():
    sample_string = "hello hello world"
    substring = "hello"
    count = count_substring(sample_string, substring)
    print(f"Occurrences of '{substring}': {count}")

if __name__ == "__main__":
    main()
