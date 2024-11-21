'''
    @Author: VEMULA DILEEP
    @Date: 25-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:40
    @Title : Python program to find the repeated items of a tuple
'''

def find_repeated_items(t):
    """
    Description:
        This function finds and returns repeated items in a tuple.
    Parameters:
        t : tuple
    Return:
        list : a list of repeated items
    """
    return [item for item in set(t) if t.count(item) > 1]

def main():
    t = (1, 2, 3, 2, 4, 5, 1, 6)
    repeated_items = find_repeated_items(t)
    print("Repeated Items:", repeated_items)

if __name__ == "__main__":
    main()
