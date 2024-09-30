'''
    @Author: VEMULA DILEEP
    @Date: 30-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:15
    @Title : Python program to count the number of characters (character frequency) in a string.
'''

def character_frequency(s):
    """
    Description:
        This function counts the frequency of each character in the string.
    Parameters:
        s : str
    Return:
        dict : character frequency dictionary
    """
    freq_dict = {}
    for char in s:
        freq_dict[char] = freq_dict.get(char, 0) + 1
    return freq_dict

def main():
    sample_string = "google.com"
    frequency = character_frequency(sample_string)
    print(f"Character frequency: {frequency}")

if __name__ == "__main__":
    main()
