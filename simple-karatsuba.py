#next step is to use listify on x and y in the fancy_multiplication function to assign values to a,b,c,d. Also need to incorporate size of the input integers n into the fancy_multiplication function

import numpy as np


def listify(z): #this function turns a number into an array of its digits. The purpose of this function is to make the individual digits accessable for the "fancy-multiply function"
  number_string = str(z) #turn the integer into a string so we can iterate through the individual characters (digits)
  temp_array = np.empty(0, dtype=int) #create an empty array so each digit can be added after every iteration of the following loop
  print(temp_array)
  for digit in number_string:
    temp_array = np.append(temp_array, (int(digit)))#notice here that you have to re-assign the np.append stuff to digit array again. This is because when you use np.append, it isn't actually updating the old array - it's creating a whole new array that includes the newly appended value. In this sense, temp_array becomes a new array with every iteration of this loop
  return temp_array

digit_array = listify(2345)
print(digit_array)
array_chunk = np.array_split(digit_array,2) #this chunks the number into two arrays
print(array_chunk)
first_half = array_chunk[0]
second_half = array_chunk[1]
print(first_half)
print(second_half)


#input: two n-digit positive integers x and y
#output: the product of x*y
#assumption: n is a power of 2 (i.e. 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8, so on...)
# def fancy_multiply(x,y):
#   if n = 1: #base case. this is the thing that all the calculations in this function should reduce to so that the algorithm doesn't keep going on forever and ever. Once calculations reduce to this, the algo with finally spit out an answer
#     return x*y
  
#   else: #if the problem doesn't reduce to the base case, then do this...
#     a, b = first_half, second_half
#     #c, d = the first and second halfs of the digits of y


    
