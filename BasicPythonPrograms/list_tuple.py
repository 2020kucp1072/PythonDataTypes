'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:35
    @Title : Python program to generate a list and tuple from comma-separated numbers
'''

def list_and_tuple():
    """ 
    Description:
        This function accepts a sequence of comma-separated numbers and generates
        a list and tuple with those numbers.
    Parameters:
        None
    Return:
        None
    """
    numbers = input("Enter comma-separated numbers: ")
    number_list = numbers.split(",")
    number_tuple = tuple(number_list)
    print("List:", number_list)
    print("Tuple:", number_tuple)

def main():
    list_and_tuple()

if __name__ == "__main__":
    main()
