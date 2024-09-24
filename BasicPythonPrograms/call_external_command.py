'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 18:25
    @Title : Python program to call an external command in Python
'''

import subprocess

def call_external_command():
    """ 
    Description:
        This function calls an external command (for example, 'ls' or 'dir').
    Parameters:
        None
    Return:
        None
    """
    result = subprocess.run(['echo', 'Hello from external command!'], capture_output=True, text=True)
    print(result.stdout)

def main():
    call_external_command()

if __name__ == "__main__":
    main()
