'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Title : Python program to count strings based on conditions
'''

def count_strings(items):
    """
    Description:
        This function counts strings with length 2 or more
        where the first and last character are the same.
    Parameters:
        items : list of strings
    Return:
        int : count of matching strings
    """
    return sum(1 for s in items if len(s) >= 2 and s[0] == s[-1])

def main():
    sample_list = ['abc', 'xyz', 'aba', '1221']
    result = count_strings(sample_list)
    print("Count:", result)

if __name__ == "__main__":
    main()
