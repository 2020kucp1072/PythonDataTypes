'''
    @Author: VEMULA DILEEP
    @Date: 30-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:50
    @Title : Python program to display formatted text.
'''

def display_formatted_text(text, width=50):
    """
    Description:
        This function formats the given text to a specified width.
    Parameters:
        text : str
        width : int
    Return:
        None
    """
    print(text.ljust(width))

def main():
    sample_text = "This is an example of formatted text."
    display_formatted_text(sample_text)

if __name__ == "__main__":
    main()
