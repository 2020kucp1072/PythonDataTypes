'''
    @Author: VEMULA DILEEP
    @Date: 26-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:45
    @Title : Python program to check whether an element exists within a tuple
'''

def element_exists(t, element):
    """
    Description:
        This function checks whether an element exists in a tuple.
    Parameters:
        t : tuple
        element : element to check existence in tuple
    Return:
        bool : True if element exists, else False
    """
    return element in t

def main():
    t = (1, 2, 3, 4, 5)
    element = 3
    exists = element_exists(t, element)
    print(f"Element {element} exists in tuple: {exists}")

if __name__ == "__main__":
    main()
