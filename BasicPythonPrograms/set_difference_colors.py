'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:15
    @Title : Python program to print a set containing colors that are not in another set
'''

def color_difference():
    """ 
    Description:
        This function prints a set containing all colors from one list that are not in another.
    Parameters:
        None
    Return:
        None
    """
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    print(color_list_1.difference(color_list_2))
    
    for item in color_list_1:
        if item not in color_list_2:
            print(item)

def main():
    color_difference()

if __name__ == "__main__":
    main()
