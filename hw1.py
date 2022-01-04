# problem 6, This saves the words of the sentence "Hi my name is Bob" into separate variables. The variables are then all printed to form the sentence.
def write_sentence():
    # "Save the words into variables"
    word_hi = "Hi"
    word_my = "my"
    word_name = "name"
    word_is = "is"
    word_bob = "Bob"

    # Print the string, it prints all of the variables given to it in a single string, and it also automatically adds spaces in between each word.
    print(word_hi, word_my, word_name, word_is, word_bob)

write_sentence()

# Problem 7, Calculates the bitwise OR of integers a and b then returns the result.  
def bit_or(a, b):
    bw_or_result = a | b
    
    binary_string = bin(bw_or_result)  # 0b...
    bits_part = binary_string[2:]
    # '|' is Python's bitwise OR operator
    return int(bits_part)

print(bit_or(2, 3))
print(bit_or(3, 10))

#  Problem 9, Calculate a weekday and hour (12-hr format) from Wednesday, January 1st 2020 at 12:00 AM (Midnight) given a number of hours (num_hours) returns the result as a readable string.
def calculate_day(num_hours):
    # names starting from Wednesday
    weeks = ["Wednesday","Thursday","Friday",
             "Saturday","Sunday","Monday","Tuesday"]

    # count days
    days = num_hours // 24

    # name index in weeks list
    week_index = days % 7

    # week name
    week = weeks[week_index]

    # remaining hours after removing days count
    remaining_hours = num_hours % 24

    # hours for name
    hours = remaining_hours %12

    # checking hours is 0 or not first, it helps to assume midnight or afternoon, such as 12AM or 12PM
    # Day starts at 12AM,and continues 1AM,2AM,...,11AM
    # Afternoon starts at 12PM and continues 12PM,...,11PM
    if(hours==0):
        hours=12

    # if remaining hours for week below 12, it means before afternoon 12PM
    if(remaining_hours>12):
        time = ' at ' + str(remaining_hours-12) + ' PM'
    else:
        time = ' at ' + str(remaining_hours) + ' AM'
    result = week + time
    return result
print(calculate_day(0))
print(calculate_day(1000))

# Problem 9, Calculates volume of spheres and cones
# Parameters: shape can only be either 'sphere' or 'cone'; dimensions tuple whose size depends on shape argument; sphere tuple with 1 member; cone tuple with 2 members; Returns string value, either the volume or a message

def calculate_volume(shape, dimensions):
    # Input checking
    if shape not in ("sphere", "cone"):
        return "Invalid Shape"

    # Volume calculation
    if shape == "sphere":
        r = dimensions[0]
        volume = (4 / 3) * 3.14 * (r ** 3)

    elif shape == "cone":
        r = dimensions[0]
        h = dimensions[1]
        volume = (1 / 3) * 3.14 * (r ** 2) * h

    # Preparing the result
    return round(volume,2)

print(calculate_volume('sphere', (5,)))
print(calculate_volume('cone', (3,7)))
print(calculate_volume('prism', (2,2,1)))

