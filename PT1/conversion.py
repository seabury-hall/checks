# Task: write a main function that CALLS each of these 4 functions
# For each call, ask the user for the input unit, then print a nicely formatted
# message that communicates the conversion
# DO NOT change the functions, just call them!


def knots_to_mph(knots):
    mph = knots * 1.15078
    return mph

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def days_to_seconds(days):
    seconds = days * 24 * 60 * 60
    return seconds

def miles_to_km(miles):
    kilometers = miles * 1.60934
    return kilometers