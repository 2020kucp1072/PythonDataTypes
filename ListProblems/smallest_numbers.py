'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Title : Python program to get the smallest number from a list
'''

def smallest_number(items):
    """
    Description:
        This function returns the smallest number from a list.
    Parameters:
        items : list of numbers
    Return:
        int : smallest number
    """
    return min(items)

def main():
    sample_list = [5, 1, 8, 2]
    result = smallest_number(sample_list)
    print("Smallest Number:", result)

if __name__ == "__main__":
    main()
