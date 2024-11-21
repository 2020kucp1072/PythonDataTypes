'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 20:25
    @Title : Python program to create an intersection of sets
'''

def intersection_of_sets(set1, set2):
    """
    Description:
        This function finds the intersection of two sets.
    Parameters:
        set1 (set): First set
        set2 (set): Second set
    Return:
        set: Intersection of both sets
    """
    return set1.intersection(set2)

def main():
    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    result = intersection_of_sets(set1, set2)
    print("Intersection:", result)

if __name__ == "__main__":
    main()
