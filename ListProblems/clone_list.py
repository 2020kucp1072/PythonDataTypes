'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Title : Python program to clone a list
'''

def clone_list(items):
    """
    Description:
        This function creates a copy of the list.
    Parameters:
        items : list of elements
    Return:
        list : cloned list
    """
    return items.copy()

def main():
    sample_list = [1, 2, 3, 4, 5]
    result = clone_list(sample_list)
    print("Cloned List:", result)

if __name__ == "__main__":
    main()
