'''
    @Author: VEMULA DILEEP
    @Date: 26-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:05
    @Title : Python program to reverse a tuple
'''

def reverse_tuple(t):
    """
    Description:
        This function reverses a tuple.
    Parameters:
        t : tuple
    Return:
        tuple : reversed tuple
    """
    return t[::-1]

def main():
    t = (1, 2, 3, 4, 5)
    result = reverse_tuple(t)
    print("Reversed Tuple:", result)

if __name__ == "__main__":
    main()
