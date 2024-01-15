#input: two n-digit positive integers x and y
#output: the product of x*y
#assumption: n is a power of 2 (i.e. 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8, so on...)


def listify(z): #this function turns a number into a list of its digits. The purpose of this function is to make the individual digits accessable for the "fancy-multiply function"
  number_string = str(z) #turn the integer into a string so we can iterate through the individual characters (digits)
  digit_list = [] #create an empty list so each digit can be added after every iteration of the following loop
  for digit in number_string:
    digit_list.append(int(digit))
  return digit_list


def fancy-multiply(x,y):
  if n = 1: #base case. this is the thing that all the calculations in this function should reduce to so that the algorithm doesn't keep going on forever and ever. Once calculations reduce to this, the algo with finally spit out an answer
    return x*y
  
  else: #if the problem doesn't reduce to the base case, then do this...
    #a, b = the first and second halfs of the digits of x
    #c, d = the first and second halfs of the digits of y
    
