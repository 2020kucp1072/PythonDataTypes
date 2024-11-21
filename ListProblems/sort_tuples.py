'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Title : Python program to sort tuples by last element
'''

def sort_tuples(items):
    """
    Description:
        This function sorts a list of tuples by the last element.
    Parameters:
        items : list of tuples
    Return:
        list : sorted list of tuples
    """
    return sorted(items, key=lambda x: x[-1])

def main():
    sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    result = sort_tuples(sample_list)
    print("Sorted List:", result)

if __name__ == "__main__":
    main()
