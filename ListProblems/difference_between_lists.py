'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Title : Python program to find the difference between two lists
    
'''

def difference_between_lists(list1, list2):
    """
    Description:
        This function returns the difference between two lists.
    Parameters:
        list1 : list
        list2 : list
    Return:
        list : elements in list1 but not in list2
        
    """
    return list(set(list1) - set(list2))

def main():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = difference_between_lists(list1, list2)
    print("Difference:", result)

if __name__ =="__main__":
    main()
