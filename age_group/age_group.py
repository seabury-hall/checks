"""Write a Python program called "age_group.py" that takes a person's age as input 
and prints the relative age group as per the table below:

Toddler: 0-2 years old
Child: 3-12 years old
Teenager: 13-19 years old
Adult: 20-64 years old
Senior: 65-895 years old
Yoda: 896 and above

If the user enters a negative number, your 
program should output: "Please enter a valid age"
"""


def main():
    age = int(input("Enter your Age: "))
    
    group = age_group(age)


def age_group(age):
    if age < 0:
        print("Please enter a valid age")
    elif age >= 0 and age <= 2:
        print("Toddler")
    elif age >= 3 and age <= 12:
        print("Child")
    elif age >= 13 and age <= 19:
        print("Teenager")
    elif age >= 20 and age <= 64:
        print("Adult")
    elif age >= 65 and age <=895:
        print("Senior")
    elif age >= 896:
        print("Yoda")
    else:
        print()


if __name__ == "__main__":
    main()