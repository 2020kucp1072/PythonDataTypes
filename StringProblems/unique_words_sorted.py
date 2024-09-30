'''
    @Author: VEMULA DILEEP
    @Date: 30-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:40
    @Title : Python program to print unique words in sorted form.
'''

def unique_sorted_words(input_string):
    """
    Description:
        This function prints the unique words from a comma-separated string in sorted order.
    Parameters:
        input_string : str
    Return:
        None
    """
    words = input_string.split(", ")
    unique_words = sorted(set(words))
    print(", ".join(unique_words))

def main():
    sample_words = "red, white, black, red, green, black"
    unique_sorted_words(sample_words)

if __name__ == "__main__":
    main()
