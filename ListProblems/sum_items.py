'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Title : Python program to sum all the items in a list
'''

def sum_list(items):
    """
    Description:
        This function returns the sum of all items in a list.
    Parameters:
        items : list of numbers
    Return:
        int : sum of all items
    """
    return sum(items)

def main():
    sample_list = [1, 2, 3, 4, 5]
    result = sum_list(sample_list)
    print("Sum:", result)

if __name__ == "__main__":
    main()
