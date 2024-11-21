'''
    @Author: VEMULA DILEEP
    @Date: 26-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:30
    @Title : Python program to unpack a tuple in several variables
'''

def unpack_tuple(t):
    """
    Description:
        This function unpacks a tuple into separate variables.
    Parameters:
        t : tuple
    Return:
        tuple : individual elements of the tuple
    """
    a, b, c, d = t
    return a, b, c, d

def main():
    t = (1, 2, 3, 4)  
    a, b, c, d = unpack_tuple(t)
    print(f"Unpacked Values: a={a}, b={b}, c={c}, d={d}")

if __name__ == "__main__":
    main()
