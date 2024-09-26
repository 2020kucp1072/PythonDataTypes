'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Title : Python program to remove specific elements from a list
'''

def remove_specific_elements(items):
    """
    Description:
        This function removes the 0th, 4th, and 5th elements from the list.
    Parameters:
        items : list
    Return:
        list : modified list
    """
    return [item for index, item in enumerate(items) if index not in (0, 4, 5)]

def main():
    sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    result = remove_specific_elements(sample_list)
    print("Modified List:", result)

if __name__ == "__main__":
    main()
