# problem 5, write a method named calculate_letter() to letter grade
def calculate_letter(s):
    # grade standard same as given form
    if(s >= 93):
        return 'A'
    elif(s >= 90 and s < 93):
        return 'A-'
    elif(s >= 87 and s < 90):
        return 'B+'
    elif(s >= 83 and s < 87):
        return 'B'
    elif(s >= 80 and s < 83):
        return 'B-'
    elif(s >= 77 and s < 80):
        return 'C+'
    elif(s >= 73 and s < 77):
        return 'C'
    elif(s >= 70 and s < 73):
        return 'C-'
    elif(s >= 50 and s < 70):
        return 'D'
    elif(s >= 0 and s < 50):
        return 'F'
# input any grade, it will letter the grade.   
print("The grade is",calculate_letter(98))

# problem 6, write a method named is_leap(year) 
def is_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else: 
            return True
    else:
        return False
year = 2021
if(is_leap(year)):
    print('%d is a leap year.' %(year))
else:
    print('%d is not a leap year.' %(year))

# problem 7, write a method named is_trangle() to check if a number is a triangular number
# implementation to check if a number is a triangular number using simple approach.
# returns True if 'num' is triangular, else False
# function definition
def is_triangle(num):
    # base case
	if num < 0:
	    return False
	# a triangular number must be sum of first n natural numbers
	add = 0
	term = 1
    # loop iterates till the number
	while add <= num:
        # add it up
	    add += term                
	    if add == num:
	        return True
        # update the term
	    term += 1;                
	return False


# input the number
number = 92
# function calling
if is_triangle(number):
    print("%d is a triangular number." %number)
else:
    print("%d is NOT a triangular number." %number)

# problem 8, write a method named triangle_num() to sum up all the triangular numbers.
# code from problem 7
def is_triangle(num):
    # base case
	if num < 0:
	    return False
	# a triangular number must be sum of first n natural numbers
	add = 0
	term = 1
    # loop iterates till the number
	while add <= num:
        #add it up
	    add += term                
	    if add == num:
	        return True
        #update the term
	    term += 1;                
	return False

# write a method to return the sum of all triangular numbers
def triangle_sum(lower_bound, upper_bound):
    total = 0
    # for loop iterates from lower bound to upper bound
    for i in range(lower_bound, upper_bound):
        if is_triangle(i):
            total += i
    return total    
add_all_triangular = triangle_sum(11, 56)
# print the result
print("Sum of all triangular numbers is %d."  %add_all_triangular)

# problem 9, write a method named random_gen() to generate a list of random numbers
import random
def random_gen(n):
    # creat a empty list
    list_random = []
    # use for loop to generate random numbers
    for i  in range(n):
        num = random.randint(1,9)
        # appending numbers to the empty list created previously
        list_random.append(num)
    return list_random
# give a random size then print the random list out

print('The random list with given size is ', random_gen(2))

# problem 10, write a method named digit_sum() then return an integer
def digit_sum(num):
    # check every time if our sum is less than 9 (i,e single digit)
    # if it is not, again calculate the sum gain or break the loop
    while True:
        sum_cal = 0
        while num > 0:
            remainer = num % 10
            # take units digit and add it to sum and divide it by 10
            sum_cal += remainer
            # getting every digit and adding it to the sum
            num = num // 10
        if sum_cal < 10:
            break
        else:
            num = sum_cal
    return sum_cal

print("The sum is ",digit_sum(44))