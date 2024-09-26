'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Title : Python function to check common members in two lists
'''

def have_common_member(list1, list2):
    """
    Description:
        This function checks if there is at least one common member in two lists.
    Parameters:
        list1 : list
        list2 : list
    Return:
        bool : True if there is a common member, else False
    """
    return bool(set(list1) & set(list2))

def main():
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    result = have_common_member(list1, list2)
    print("Common Member Exists:", result)

if __name__ == "__main__":
    main()
