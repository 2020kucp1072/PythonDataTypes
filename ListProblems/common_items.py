'''
    @Author: VEMULA DILEEP
    @Date: 25-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:45
    @Title : Python program to find common items from two lists
'''

def find_common_items(list1, list2):
    """
    Description:
        This function finds common items between two lists.
    Parameters:
        list1 : list
        list2 : list
    Return:
        list : list of common items
    """
    return list(set(list1).intersection(set(list2)))

def main():
    list1 = [1, 2, 3]
    list2 = [2, 3, 4]
    result = find_common_items(list1, list2)
    print("Common Items:", result)

if __name__ == "__main__":
    main()
