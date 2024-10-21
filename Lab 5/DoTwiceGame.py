r'''
Task Description: 
      In this task, you need to design one program of performing a “Do Twice” game. 
      The intuitive idea is that when user wants to do one operation, your program 
      helps him to do twice. More detailed procedure is as follows: 
      a.)	Design one function double(x) to calculate the double (2*x) of one number x. 
      b.)	Design one function square(x) to calculate the square (x*x) of one number x.
      c.)	Design one function cube(x) to calculate the cube (x*x*x) of one number x. 
      d.)	Design one program to ask user to input one number and another 
            operation number (1 for Double, 2 for Square, 3 for Cube). 
            Once user inputs these information, your program needs to perform the operation 
            twice to user. 
            For example, if user inputs option 1 to double the number x, 
            your program should output double(double(x)) (e.g. 4x) for user. If the user 
            inputs option 2 to square x, your program should output square(square(x)) (e.g. x4)). 
            If the user inputs 3 to cube the x, your program should output cube(cube(x)) (e.g. x9). 

Hint: 
      You need to write one higher order function doTwice(func, x) to perform the function func 
      twice for given number x. 

Note:
      a. Options: 
            1 - double 
            2 - square 
            3 - cube
      b. Your output should be in ONE line 

Running example:
      C:\INF002\Lab5\DoTwiceGame> python DoTwiceGame.py 4 1
      16

      C:\ INF002\Lab5\DoTwiceGame> python DoTwiceGame.py 4 2
      256

      C:\ INF002\Lab5\DoTwiceGame> python DoTwiceGame.py 4 4
      It cannot be supported!
'''
import sys

# write your code here
# you can use sys.argv[1] to get the first input argument.
# sys.argv[2] is the second argument, etc.

def double(x):
    return x*2

def square(x):
    return x**2

def cube(x):
    return x**3

def doTwice(func, x):
    return func(func(x))
 
def DoTwiceGame():
    try:
        x = int(sys.argv[1])
        operation = int(sys.argv[2])
        if operation == 1:
            print(doTwice(double, x))
        elif operation == 2:
            print(doTwice(square, x))
        elif operation == 3:
            print(doTwice(cube, x))
        else:
            print("It cannot be supported!")
            
    except ValueError:
        print("Your input is invalid!")
        return

if __name__=='__main__':
      DoTwiceGame()