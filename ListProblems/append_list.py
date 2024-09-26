'''
    @Author: VEMULA DILEEP
    @Date: 25-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:55
    @Title : Python program to append a list to another list
'''

def append_list(list1, list2):    
    """
    Description:
        This function appends list1 to list2.
    Parameters:
        list1 : list
        list2 : list
    Return:
        list : concatenated list
    """
    return list2 + list1

def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    result = append_list(list1, list2)
    print("Appended List:", result)

if __name__ == "__main__":
    main()
