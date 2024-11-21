'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:40
    @Title : Python program to display the first and last colors from a list
'''

def first_and_last_color():
    """ 
    Description:
        This function displays the first and last colors from a predefined list.
    Parameters:
        None
    Return:
        None
    """
    color_list = ["Red", "Green", "White", "Black"]
    print("First color:", color_list[0])
    print("Last color:", color_list[-1])

def main():
    first_and_last_color()

if __name__ == "__main__":
    main()
