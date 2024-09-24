'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:00
    @Title : Python program to check if a specified value is contained in a group of values
'''

def check_value_in_list():
    """ 
    Description:
        This function checks if a specified value is contained in a given list.
    Parameters:
        None
    Return:
        None
    """
    values = [1, 5, 8, 3]
    number = int(input("Enter a number to check: "))
    print(number, "->", values, ":", number in values)

def main():
    check_value_in_list()

if __name__ == "__main__":
    main()
