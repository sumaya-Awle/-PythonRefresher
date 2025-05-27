#Question 1
days=int(input("Enter the number of days: "))

seconds_in_a_day=60*60*24

seconds=int(seconds_in_a_day*days)

print(f"There are {seconds} seconds in {days} days")

#Question 2
import math
radius=int(input("Enter the radius of the sphere: "))

rCubbed = radius**3

volume=(4/3)*math.pi*rCubbed


print("The volume of the sphere is: ",volume)

#Question 3
# Function to calculate perimeter
def calculate_perimeter(side):
    return side * 4

# Function to calculate area
def calculate_area(side):
    return side * side


side_length = int(input("Enter the side length of the square: "))

perimeter = calculate_perimeter(side_length)
area = calculate_area(side_length)

print("The perimeter of the square is", perimeter)
print("The area of the square is", area)

#Question 4
def case_type(letter):
    if letter.isupper():
        return "Uppercase"
    elif letter.islower():
        return "Lowercase"
    else:
        return "Please enter a letter"

char = input("Enter a single character: ")

result=(case_type(char))

print("The letter you've entered is", result)

#Question 5
x=0
y=20

while y>=6:
    y=(y-4)
    x=x+(2/y)

print(x)

#Question 6
values=[]
count=0
while count<5:

    num=int(input("Enter a number: "))
    values.append(num)
    count+=1

average=sum(values)/5

print("The average is", average)