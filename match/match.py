from math import pi

def main():
    # Main controls the flow of the program
    
    # Get Input
    shape = input("Enter a shape name: ")
    
    # Calculaute Area of the shape that is inputted
    area = calculate_area(shape)

    # Print Area of the shape the user chose 
    print(f"The area of the {shape} is: {area}")



def calculate_area(shape):

    # Fix the bug in the code below  
    # re-write this code to use a "match" statement
    # Make one improvement to the functionality of this code


    match shape:
        
        case 'square':
            side = input("Enter the length of the side: ")
            return int(side) ** 2
        
        case 'rectangle':
            length = input("Enter the length: ")
            width = side = input("Enter the width: ")
            return length * width
        
        case 'circle':
            radius = input("Enter the radius: ")
            return pi * radius ** 2
        
        case 'triangle':
            base = input("Enter the base: ")
            height = input("Enter the height: ")
            return 0.5 * base * height
        
        case 'polygon':
            sides = input("How many sides: ")
            inscribedCircle = input("Inscribed Circle: ")
            return .5 * int(sides) * int(inscribedCircle)
        
        case _:
            return "Shape not supported!"


# Do not change below this line!
main()
