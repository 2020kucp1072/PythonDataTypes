'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:10
    @Title : Python program to concatenate all elements in a list into a string
'''

def concatenate_list_elements(elements):
    """ 
    Description:
        This function concatenates all elements in a list into a single string.
    Parameters:
        elements: List of elements
    Return:
        str: Concatenated string
    """
    return ''.join(elements)

def main():
    elements = ['a', 'b', 'c', 'd']
    result = concatenate_list_elements(elements)
    print("Concatenated String:", result)

if __name__ == "__main__":
    main()
