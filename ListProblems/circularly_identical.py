'''
    @Author: VEMULA DILEEP
    @Date: 25-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:00
    @Title : Python program to check if two lists are circularly identical
'''

def are_circularly_identical(list1, list2):
    """
    Description:
        This function checks if two lists are circularly identical.
    Parameters:
        list1 : list
        list2 : list
    Return:
        bool : True if circularly identical, else False
    """
    return len(list1) == len(list2) and ''.join(map(str,list1)) in ''.join( map(str,list2 * 2))

def main():
    list1 = [1, 2, 3]
    list2 = [2, 3, 1]
    result = are_circularly_identical(list1, list2)
    print("Circularly Identical:", result)

if __name__ == "__main__":
    main()
