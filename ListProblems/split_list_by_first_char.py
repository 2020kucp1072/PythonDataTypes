'''
    @Author: VEMULA DILEEP
    @Date: 25-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:05
    @Title : Python program to split a list based on the first character of word
'''

from collections import defaultdict

def split_by_first_char(words):
    """
    Description:
        This function splits a list of words based on the first character.
    Parameters:
        words : list of strings
    Return:
        dict : dictionary with first character as key and words as values
    """
    result = defaultdict(list)
    for word in words:
        result[word[0]].append(word)
    return dict(result)

def main():
    sample_list = ['apple', 'banana', 'avocado', 'berry', 'cherry']
    result = split_by_first_char(sample_list)
    print("Split List:", result)

if __name__ == "__main__":
    main()
