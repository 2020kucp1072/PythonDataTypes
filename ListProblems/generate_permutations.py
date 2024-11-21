'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Title : Python program to generate all permutations of a list
'''

from itertools import permutations

def generate_permutations(items):
    """
    Description:
        This function generates all permutations of a list.
    Parameters:
        items : list
    Return:
        list : all permutations of the input list
    """
    return list(permutations(items))

def main():
    sample_list = [1, 2, 3]
    result = generate_permutations(sample_list)
    print("Permutations:", result)

if __name__ == "__main__":
    main()
