'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 20:10
    @Title : Python program to create a symmetric difference of sets
'''

def symmetric_difference_of_sets(set1, set2):
    """
    Description:
        This function returns the symmetric difference of two sets.
    Parameters:
        set1 : set
        set2 : set
    Return:
        set : symmetric difference of set1 and set2
    """
    return set1.symmetric_difference(set2)

def main():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    result = symmetric_difference_of_sets(set1, set2)
    print("Symmetric Difference:", result)

if __name__ == "__main__":
    main()
