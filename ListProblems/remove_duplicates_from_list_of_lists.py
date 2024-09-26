'''
    @Author: VEMULA DILEEP
    @Date: 25-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:10
    @Title : Python program to remove duplicates from a list of lists
'''

def remove_duplicates(lists):
    """
    Description:
        This function removes duplicate lists from a list of lists.
    Parameters:
        lists : list of lists
    Return:
        list : list of unique lists
    """
    seen = []
    for item in lists:
        if item not in seen:
            seen.append(item)
    return seen

def main():
    sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    result = remove_duplicates(sample_list)
    print("Unique Lists:", result)

if __name__ == "__main__":
    main()
