'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 20:00
    @Title : Python program to create a set
'''

def create_set():
    """
    Description:
        This function creates a set and returns it.
    Parameters:
        None
    Return:
        set: The created set
    """
    my_set = set()
    my_set.add(1)
    my_set.add(2)
    my_set.add(3)
    my_set.add(4)
    my_set.add(5)
    my_set.add(6)
    
    
    return my_set

def main():
    result = create_set()
    print("Created Set:", result)

if __name__ == "__main__":
    main()
