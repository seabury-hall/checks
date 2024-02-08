from math import pi

def main():
    # Main controls the flow of the program
    # TODO: Replace this comment with a description of what the line of code below does  
    shape = input("Enter a shape name: ")
    
    # Calculaute Area
    # TODO: Replace this comment with a description of what the line of code below does  
    area = calculate_area(shape)

    # Print Area
    # TODO: Replace this comment with a description of what the line of code below does  
    print(f"The area of the {shape} is: {area}")



def calculate_area(shape):

    # TODO: Fix the bug in the code below  
    # TODO: re-write this code to use a "match" statement
    # TODO: Make one improvement to the functionality of this code


    if shape == 'square':
        side = input("Enter the length of the side: ")
        return side ** 2
    
    elif shape == 'rectangle':
        length = input("Enter the length: ")
        width = side = input("Enter the width: ")
        return length * width
    
    elif shape == 'circle':
        radius = input("Enter the radius: ")
        return pi * radius ** 2
    
    elif shape == 'triangle':
        base = input("Enter the base: ")
        height = input("Enter the height: ")
        return 0.5 * base * height
    
    else:
        return "Shape not supported!"


# Do not modify below this line!
main()
