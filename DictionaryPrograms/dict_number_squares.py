'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:45
    @Title : Python program to generate and print a dictionary containing numbers and their squares
'''

def generate_square_dict(n):
    """
    Description:
        This function generates a dictionary where keys are numbers and values are their squares.
    Parameters:
        n (int): The number up to which squares are generated.
    Return:
        None
    """
    square_dict = {}
    
    for i in range(1,(n+1)):
        square_dict[i]=i*i
    print(f"Dictionary for n={n}:", square_dict)

def main():
    n = int(input("Enter the value of n: "))
    generate_square_dict(n)

if __name__ == "__main__":
    main()
