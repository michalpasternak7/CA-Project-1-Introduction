def narcissistic_number(number):

    digit_len = len(str(number))
    original_number = number
    sum_of_powers = 0
    
    while number > 0:
        digit = number % 10
        power_of_digit = digit
        
        for power in range(digit_len - 1):
            power_of_digit *= digit

        sum_of_powers += power_of_digit

        number = int((number - digit) / 10)
    
    return sum_of_powers == original_number

print(narcissistic_number(1634))
print(narcissistic_number(153))
print(narcissistic_number(4322))