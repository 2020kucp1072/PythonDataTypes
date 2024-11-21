'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:50
    @Title : Python program to display the calendar for a given month and year
'''

import calendar

def display_calendar():
    """ 
    Description:
        This function accepts a year and month as input and prints the corresponding calendar.
    Parameters:
        None
    Return:
        None
    """
    year = int(input("Enter year: "))
    month = int(input("Enter month: "))
    print(calendar.month(year, month))

def main():
    display_calendar()

if __name__ == "__main__":
    main()
