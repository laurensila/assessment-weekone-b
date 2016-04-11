# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".

def hello_world():
    print "Hello World"


# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.

def hello_name(name):
    print "Hi" + str(name)


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def multiplication(num1, num2):
    return num1 * num2


# 4. Write a function that takes a string and an integer and
#    prints the string that many times

def string_printer(x, count):
    print str(x) * count

# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def high_low(num1):
    if num1 > 0:
        print "Higher than 0"
    elif num1 < 0:
        print "Lower than 0"
    elif num1 == 0:
        print "Zero"


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def divide_by_three(num1):
    if num1 % 3 == 0:
        return True
    else:
        return False


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def space_counter(some_string):



# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def tip_calculator(meal, custom_tip):
  
    meal = int()
    tip = .15
    custom_tip = int()
    total = meal + meal * tip

    if custom_tip > 0:
        print meal + meal * custom_tip
    else:
        print total


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.

def even_odd(num1):
    num_info = []
    
    num1 > 0 = negative
    num1 < 0 = positive
    num1 % 3 == 0 = odd
    num1 % 2 == 0 = even
    
    if num1 = negative:
        num_info.append("Negative")
    else:
        num_info.append("Positive")

    if num1 = odd:
        num_info.append("Odd")
    else:
        num_info.append("Even")
    
    print num_info[]


#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.
"""I wasn't really sure how to show the unpacking of the list. I think I'm still a bit lost on how to unpack a list."""

def even_odd(20):

    num_info["Positive", "Even"]
    
    num_info[0] = sign
    num_info[1] = parity

    print sign + parity



################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.
