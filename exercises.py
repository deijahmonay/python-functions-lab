# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.

def calculate_area_triangle(base,height):
    area = (base * height) / 2
    return area

print('Exercise 1:', calculate_area_triangle(10, 5))
print('Exercise 1: EXTRA', calculate_area_triangle(30, 15))

# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
def simple_interest(principal, rate, time):
    return (principal * rate * time ) / 100

# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.

print('Exercise 2:', simple_interest(1000, 5, 2))
print('Exercise 2:', simple_interest(1500, 3.5, 5))

# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
def apply_discount(price, discount_percentage):
    return price - (price * discount_percentage / 100)
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.



print('Exercise 3:', apply_discount(100, 25))
print('Exercise 3:', apply_discount(80, 10))


# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
def convert_temperature(temperature, unit):
    if unit == 'C':
        return (temperature * 9/5) + 32
    else:
        return (temperature - 32 ) * 5/9
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.



print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
def sum_to(n):
    return sum(num for num in range(1, n + 1)) 
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.

print('Exercise 5:', sum_to(6))
print('Exercise 5:', sum_to(10))
print('Exercise 5:', sum_to(20))


# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
def largest(a, b, c):
    return max(a, b, c) # https://www.w3schools.com/python/ref_func_max.asp
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.



print('Exercise 6:', largest(1, 2, 3))
print('Exercise 6:', largest(10, 4, 2))
print('Exercise 6:', largest(45, 54, 32))


