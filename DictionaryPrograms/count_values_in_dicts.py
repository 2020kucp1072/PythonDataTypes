'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 19:20
    @Title : Python program to count the values associated with a key in a list of dictionaries
'''

def count_success(data):
    """
    Description:
        This function counts how many dictionaries have the value 'True' for the 'success' key.
    Parameters:
        data (list): List of dictionaries to check.
    Return:
        None
    """
    count =0
    
    for item in data:
            if item.get('success')==True:
                count+=1
                
    print(f"Count of 'success' as True:", count)

def main():
    data = [{'id': 1, 'success': True, 'name': 'Lary'}, 
            {'id': 2, 'success': False, 'name': 'Rabi'}, 
            {'id': 3, 'success': True, 'name': 'Alex'}]
    count_success(data)

if __name__ == "__main__":
    main()
