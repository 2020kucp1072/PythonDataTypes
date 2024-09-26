'''
    @Author: VEMULA DILEEP
    @Date: 26-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:00
    @Title : Python program to slice a tuple
'''

def slice_tuple(t, start, end):
    """
    Description:
        This function slices a tuple from start to end indices.
    Parameters:
        t : tuple
        start : starting index
        end : ending index
    Return:
        tuple : sliced tuple
    """
    return t[start:end]

def main():
    t = (1, 2, 3, 4, 5, 6, 7, 8)
    start, end = 2, 5
    result = slice_tuple(t, start, end)
    print("Sliced Tuple:", result)

if __name__ == "__main__":
    main()
