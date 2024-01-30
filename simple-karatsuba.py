#The goal of this program is to make a multiplication function that takes in two positive numbers with n-digits, and return the product of those two positive numbers. This is all done assuming that n is a power of 2 (i.e. 2^0, 2^1, 2^2, etc.)

import numpy as np


def listify(z): #this function turns a number into an array of its digits. The purpose of this function is to make the individual digits accessable for the "fancy-multiply function"
  number_string = str(z) #turn the integer into a string so we can iterate through the individual characters (digits)
  temp_array = np.empty(0, dtype=int) #create an empty array so each digit can be added after every iteration of the following loop
  print(temp_array)
  for digit in number_string:
    temp_array = np.append(temp_array, (int(digit)))#notice here that you have to re-assign the np.append stuff to digit array again. This is because when you use np.append, it isn't actually updating the old array - it's creating a whole new array that includes the newly appended value. In this sense, temp_array becomes a new array with every iteration of this loop
  return temp_array



#testing---------------------------------------------------------
#----------------------------------------------------------------
# digit_array = listify(2345) #use listify function to turn number into array of its digits
# print(digit_array) #check that listify function actually turns numbers into arrays
# array_chunk = np.array_split(digit_array,2) #this chunks the number into two arrays
# print(array_chunk)#check that array is turned into two halves
# first_half = array_chunk[0]
# second_half = array_chunk[1]
# print(first_half) #check that array chunking worked for first half
# print(second_half) #check that array chunking worked for second half
#end of testing--------------------------------------------------
#----------------------------------------------------------------

#----------------------------------------------------------------
#----------------------------------------------------------------
#Beginning of code for the multiplication function
#----------------------------------------------------------------
#----------------------------------------------------------------
#input: two n-digit positive integers x and y
#output: the product of x*y
#assumption: n is a power of 2 (i.e.
#  2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8, so on...)



entry1 = int(input("Enter a number: ")) #first number user enters, which will be passed through the fancy_multiply function
entry2 = int(input("Enter another number: "))#second number user enters, which will be passed through the fancy_multiply function
array1 = listify(entry1) #turn entry1 into array of its digits
array2 = listify(entry2) #turn entry2 into array of its digits
print(array1) #quick test that listify turned entry1 into an array
print(array2) #quick test that listify turned entry2 into an array
array1_chunk = np.array_split(array1,2) #split array 1 into 2 equal chunks
array2_chunk = np.array_split(array2,2) #split array 2 into 2 equal chunks
n = len(array1) #this will tell you the number of digits in entry1. For now, I'll ignore that there should be a check that len(array1) must equal len(array2)
print(n)#quick test that n is the correct number of digits
#question: How should the block above all be locally defined inside the fancy multiply function? Or does it belong out of the fancy multiply function's scope. For now I'll just keep it out of scope

def fancy_multiply(x,y):
  if n == 1: #base case. this is the thing that all the calculations in this function should reduce to so that the algorithm doesn't keep going on forever and ever. Once calculations reduce to this, the algo with finally spit out an answer
    return x*y
  
  else: #if the problem doesn't reduce to the base case, then do this...
    a, b = (array1_chunk[0]), (array1_chunk[1]) #first and second halfs of x
    c, d = (array2_chunk[0]), (array2_chunk[1]) #first and second halfs of y
    print('a:', a,'b:', b,'c:',c,'d:',d)
    ac, ad, bc, bd = a*c, a*d, b*c, b*d
    print(ac, ad, bc, bd)
    return (10**n)*ac + int(10**(n/2))*(ad +bc) + bd


result = fancy_multiply(entry1, entry2)
print(result)