'''
    @Author: VEMULA DILEEP
    @Date: 26-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:25
    @Title : Python program to create a tuple with different data types
'''

def create_mixed_tuple():
    """
    Description:
        This function creates a tuple with different data types.
    Return:
        tuple : a tuple containing elements of various data types
    """
    return (1, "Hello", 3.14, True)

def main():
    result = create_mixed_tuple()
    print("Tuple with Different Data Types:", result)

if __name__ == "__main__":
    main()
