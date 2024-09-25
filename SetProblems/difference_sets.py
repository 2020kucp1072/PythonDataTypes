'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 20:05
    @Title : Python program to create a difference of sets
'''

def difference_of_sets(set1, set2):
    """
    Description:
        This function returns the difference of two sets (set1 - set2).
    Parameters:
        set1 : set
        set2 : set
    Return:
        set : difference of set1 and set2
    """
    return set1.difference(set2)

def main():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    result = difference_of_sets(set1, set2)
    print("Difference:", result)

if __name__ == "__main__":
    main()
