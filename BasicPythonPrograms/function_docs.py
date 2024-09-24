'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:45
    @Title : Python program to print the documentation of Python built-in function
'''

def print_function_docs():
    """ 
    Description:
        This function prints the documentation of the abs() function.
    Parameters:
        None
    Return:
        None
    """
    print("Documentation for abs function:")
    print(abs.__doc__)

def main():
    print_function_docs()

if __name__ == "__main__":
    main()
