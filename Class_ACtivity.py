def is_narc(n):
    """Check if a number is narc."""
    num_str = str(n)
    num_digits = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    return sum_of_powers == n

def print_narcis_numbers(start, end):
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1):
        if is_narc(num):
            print(num)

print_narcis_numbers(1000, 5000)
"""Submit your response here: https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u """

# Syntax error in 1, 10, 12, 13. Added ':'
# Wrong assignment of value to variable in lines 3, 4. Changed '==' to '='
# IN line 16, function 'print_narc_numbers' not defined, Chanegd it to 'print_narcis_numbers'
# IN line 13, function 'is_narcissistic' not defined. Changed it to 'is_narc'
# In line 10, missing ',' between start and end.
# IN line 6, the correct power operator is '**' and not '***'

