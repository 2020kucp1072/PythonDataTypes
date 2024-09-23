'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:30
    @Title : Python program to reverse user's first and last name
'''

def reverse_name():
    """ 
    Description:
        This function accepts first and last name and prints them in reverse order.
    Parameters:
        None
    Return:
        None
    """
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(f"{last_name} {first_name}")

def main():
    reverse_name()

if __name__ == "__main__":
    main()
