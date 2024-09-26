'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Title : Python program to find words longer than n
'''

def words_longer_than_n(words, n):
    """
    Description:
        This function finds words longer than a given length n.
    Parameters:
        words : list of strings
        n : int
    Return:
        list : words longer than n
    """
    return [word for word in words if len(word) > n]

def main():
    sample_list = ['apple', 'banana', 'kiwi', 'pear']
    result = words_longer_than_n(sample_list, 4)
    print("Words longer than 4:", result)

if __name__ == "__main__":
    main()
