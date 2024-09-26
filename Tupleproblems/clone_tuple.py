'''
    @Author: VEMULA DILEEP
    @Date: 26-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:35
    @Title : Python program to create the clone of a tuple
'''

def clone_tuple(t):
    """
    Description:
        This function creates a clone (copy) of the given tuple.
    Parameters:
        t : tuple
    Return:
        tuple : a copy of the original tuple
    """
    return t[:]

def main():
    original = (1, 2, 3, 4)
    clone = clone_tuple(original)
    print("Original Tuple:", original)
    print("Cloned Tuple:", clone)

if __name__ == "__main__":
    main()
