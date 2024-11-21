'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 19:05
    @Title : Python program to print all unique values in a dictionary
'''

def print_unique_values():
    """
    Description:
        This function prints all unique values from a list of dictionaries.
    Parameters:
        None
    Return:
        None
    """
    data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
            {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    
    unique_values = set()
    
    for dic in data:
        for val in dic.values():
            unique_values.add(val)
            
    print("Unique Values:", unique_values)

def main():
    print_unique_values()

if __name__ == "__main__":
    main()
