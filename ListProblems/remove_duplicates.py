'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Title : Python program to remove duplicates from a list
'''

def remove_duplicates(items):
    """
    Description:
        This function removes duplicates from a list.
    Parameters:
        items : list of elements
    Return:
        list : list with duplicates removed
    """
    return list(set(items))

def main():
    sample_list = [1, 2, 3, 1, 2, 4]
    result = remove_duplicates(sample_list)
    print("List after removing duplicates:", result)

if __name__ == "__main__":
    main()
