'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:35
    @Title : Python program to concatenate multiple dictionaries
'''

def concatenate_dicts():
    """
    Description:
        This function concatenates multiple dictionaries into one.
    Parameters:
        None
    Return:
        None
    """
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    
    concatenated_dict = {**dic1, **dic2, **dic3}
    print("Concatenated dictionary:", concatenated_dict)

def main():
    concatenate_dicts()

if __name__ == "__main__":
    main()
