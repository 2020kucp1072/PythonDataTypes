'''
    @Author: VEMULA DILEEP
    @Date: 23-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 17:55
    @Title : Python program to calculate the number of days between two dates
'''

from datetime import date

def calculate_days_between_dates():
    """ 
    Description:
        This function calculates the number of days between two specific dates.
    Parameters:
        None
    Return:
        None
    """
    start_date = date(2014, 7, 2)
    end_date = date(2014, 7, 11)
    delta = end_date - start_date
    print(f"{delta.days} days")

def main():
    calculate_days_between_dates()

if __name__ == "__main__":
    main()
