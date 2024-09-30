'''
    @Author: VEMULA DILEEP
    @Date: 30-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:30
    @Title : Python function to find the length of the longest word in a list.
'''

def longest_word(words):
    """
    Description:
        This function returns the length of the longest word in the given list.
    Parameters:
        words : list
    Return:
        int : length of the longest word
    """
    return max(len(word) for word in words)

def main():
    word_list = ["apple", "banana", "cherry"]
    longest_length = longest_word(word_list)
    print(f"Length of the longest word: {longest_length}")

if __name__ == "__main__":
    main()
