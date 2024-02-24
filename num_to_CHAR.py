def number_to_letters(number):
    """
    we declare a result as new variable and we check for number 
    greater than 0 .
    The main reason to take remainder =(number-1) is
    to get the values from 0 to 25 in remainder 
    since 26/26 remainder is 0 so we can't get Z.
    ord(any_character) returns ascii value of that character
    chr(integer) it returns corresponding ascii valued alphabet
    next (number-1) is divided by 26 and the loop executes till number >0
            """
    result = ""
    while number > 0:
        remainder = (number - 1) % 26
        result = chr(remainder + ord('A')) + result
        number = (number - 1) // 26
    return result

def print_output(user_input):
    try:
        number = int(user_input)
        if number > 0:
            output = number_to_letters(number)
            print("Output:", output)
        else:
            print("Invalid input!")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

user_input = input("Enter a number: ")
print_output(user_input)