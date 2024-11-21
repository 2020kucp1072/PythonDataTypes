'''
    @Author: VEMULA DILEEP
    @Date: 24-09-2024
    @Last Modified by: VEMULA DILEEP
    @Last Modified time: 16:45
    @Title : Python program to sort a dictionary in ascending and descending order based on values.
'''


def sorting(di):
    
    """
    Description:
        This function sorts a dictionary based on its values in both ascending and descending order.
        
    Parameters:
        di (dict): The dictionary to be sorted.
        
    Returns:
        tuple: Two dictionaries, one sorted in ascending order, and the other in descending order.
    """
    
    asc = dict(sorted(di.items(),key=lambda item: item[1]))
    dsc = dict(sorted(di.items(),key=lambda item: item[1],reverse=True))
    return asc,dsc


def main():
       
  """
    Description:
        This function takes input from the user to create a dictionary, then sorts the dictionary in 
        ascending and descending order using the sorting() function, and prints both results.
  """
    
  n = int(input("number of keys"))
  di = {}
  for i in range(n):
      
      key = input("enter the value")
      value =int(input("enter any number"))
      di[key]=value
       
  print("Original Dictionary:",di)
  
  asc,dsc= sorting(di)
  print("Ascending order",asc)
  print("Descending order",dsc)
      
      

if __name__ =="__main__":
    main()