r'''
Task Description: 
    As a programmer, you are given a list of sales numbers from different sales 
    departments. Based on this list of numbers, you are requested to develop one 
    program to assistant your sales manager to analyse and get different 
    representations of the data. 
    
    The task you must perform is listed below: 
    a.)	Given a list of sales numbers, you need to write function scale(list1, x) 
        to return another list of scaled numbers,  where list1 is the list of sales 
        numbers and x is the scale factor. The scaled number can be calculated by 
        using the input number multiplied by the scale factor. 
        Below are some sample executions of the function:
            >>> scale([10,20,30,40],2)
                [20, 40, 60, 80]
            >>> scale([30,40, 50],0.1)
                [3.0, 4.0, 5.0]

    b.)	Given a list of sales number, you are required to write one function 
        sort(list1) to return one list of sorted sales numbers. Different to the normal 
        sorting, the sales manager requests you to sort the number based on their last 
        digit. 
        Below are some sample executions of the function:
            >>> sort([55,70,61,34,72,59])
                [70, 61, 72, 34, 55, 59]

    c.)	Given a list of sales numbers, you are required to write one function 
        goodSales(list1) to output all the good sales. The sales number is good if it is 
        above the average of the total sales numbers. 
            >>> sort([10,20,40,60,20])
                [40, 60]
            >>> sort([3,2,8,6,7])
                [8, 6, 7]

    d.)	Develop one program to allow users to input the sequence of the sales number and 
        the scale factor. Then call all the functions to show use the scaled data, sorting 
        result and good sales. 
 
Note: 
    1.	For functions a, b and c, you can optimize the function body with at most 2 lines 
        codes by using filter, map, reduce, sorted and lambda expression. See how short 
        your code can be.
    2.	Your output should be in ONE line


Running example: 
    C:\INF1002\Lab5\Sales> python salesAnalytics.py 10,20,30,40,50,60 2
    The scaled number is:  [20, 40, 60, 80, 100, 120] The sorted sales numbers are:  [10, 20, 30, 40, 50, 60] The good sales numbers are:  [40, 50, 60]
'''
import sys
# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

def scale(list1, x):
    return [i*x for i in list1]
    
def sort(list1):
    return sorted(list1, key=lambda x: x % 10)

def goodSales(list1):
    return [sale for sale in list1 if sale > (sum(list1) / len(list1))]

def SalesAnalytics():
    try:
        salesNumbers = [int(num) for num in sys.argv[1].split(",")]
        scaleFactor = int(sys.argv[2])

        scaledSalesNumbers = scale(salesNumbers, scaleFactor)
        sortedSalesNumbers = sort(salesNumbers)
        goodSalesNumbers = goodSales(salesNumbers)

        print(f"The scaled number is:  {scaledSalesNumbers} " +
              f"The sorted sales numbers are:  {sortedSalesNumbers} " +
              f"The good sales numbers are:  {goodSalesNumbers}")
            
    except ValueError:
        print("Your input is invalid.")  

if __name__=='__main__':
     SalesAnalytics()