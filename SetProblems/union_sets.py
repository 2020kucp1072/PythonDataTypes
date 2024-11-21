'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 20:00
    @Title : Python program to create a union of sets
'''

def union_of_sets(set1, set2):
    """
    Description:
        This function returns the union of two sets.
    Parameters:
        set1 : set
        set2 : set
    Return:
        set : union of set1 and set2
    """
    return set1.union(set2)

def main():
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    result = union_of_sets(set1, set2)
    print("Union:", result)

if __name__ == "__main__":
    main()
