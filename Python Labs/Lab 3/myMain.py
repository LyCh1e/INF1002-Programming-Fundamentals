r'''
Task Description:
    Develop your own math module (myMath) including eight basic functions.
    Function 1: add(x, y)         -> return the summation of x and y
    Function 2: subtraction(x, y) -> return the subtraction between x and y
    Function 3: evenNum(x)        -> return the number of even numbers in the given list
    Function 4: maximum(x)        -> return the maximum value from the given list x
    Function 5: minimum(x)        -> return the minimum value from the given list x
    Function 6: absolute(x)       -> return the absolute value of one number x
    Function 7: sumTotal(x)       -> return the summation of all the elements for a given list x
    Function 8: clear(x)          -> this function sets all the elements into 0 for a given list x

    Write one program (myMain) to import the module you have created to implement 
    the following functions.
    Step 1:
        Input: allows users to input multiple numbers. For simplicity, you can 
               assume all the input numbers are integers.
    Step 2:
        Store all the numbers into one list
    Step 3:
        a. Calculate and print out the difference between the biggest and the 
           smallest number in the list
        b. Calculate and print out the summation between the biggest and the
           smallest numbers in the list
        c. Calculate and print out the summation of all the input numbers in the list
        d. Calculate and print out the number of even numbers in the list
        e. If the smallest number in the list is smaller than 5, set all the 
        value to 0. Otherwise, remain the same. Print all the values in the list in the end.
        
    Hint:
    . To split one string, split() function can be used.
    . For instance, str = '1,2,3,4,10', list1 = str.split(',') would split 
      the string and store the numbers in the list.
    . Please keep in mind that each element in the list is a string type now. 
      You must figure out one way to convert all of them into integer.

    Please print your results according to this format:
    print("The difference is:%d The summation is:%d The summation of all input is:%d 
    The number of even numbers is:%d The values in the list are: %s" 
    % (myMath.subtraction(maxNum, minNum), myMath.add(maxNum, minNum), …)
    
    Running example: (Your output should be in ONE line)

    C:\INF1002\Lab3\MathModule>python myMain.py 12,10,11,23,25,2

    The difference is:23 The summation is:27 The summation of all input is:83 
    The number of even numbers is:3 The values in the list are: [0, 0, 0, 0, 0, 0] 
'''
import sys
import myMath

def myMain():
    if len(sys.argv) != 2:
        print("Your input is invalid.")
        return
    else:
        try:
            numbers = [int(num) for num in sys.argv[1].split(",")]       
            maxNum = float('-inf')
            minNum = float('inf')
            evenCount = 0

            maxNum = myMath.maximum(numbers)
            minNum = myMath.minimum(numbers)
            diffMaxMin = myMath.subtraction(maxNum, minNum)
            sumMaxMin = myMath.add(maxNum, minNum)

            sumTotal = myMath.sumTotal(numbers)
            evenCount = myMath.evenNum(numbers)
            
            if minNum < 5:
                myMath.clear(numbers)
            print(myMath.absolute(diffMaxMin))
            print ("The difference is:%d The summation is:%d The summation of all input is:%d The number of even numbers is:%d The values in the list are: %s" 
                   % (diffMaxMin, sumMaxMin, sumTotal, evenCount, numbers))
            
        except ValueError:
            print("Your input is invalid.")
            return
              

if __name__=='__main__':
     myMain()