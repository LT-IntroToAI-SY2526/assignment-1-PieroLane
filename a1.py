# Assignment 1: AI-Generated Python Problems
# Name: [Piero Barsanti]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
I'm learning Python basics in a high school programming class. I have some experience with [mention your previous programming language if any, or say 'I'm new to programming']. Can you create 5-7 practice problems that cover:
> - Variables and basic data types
> - Conditionals (if/elif/else)
> - Loops (for and while)
> - Functions
> - Basic list operations
> 
> Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs.]

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Personal Information Calculator]
[ Variables, basic data types, simple math
Write a program that asks for a person's name, age, and favorite number. Then display:

A greeting with their name
How old they'll be in 10 years
Their favorite number multiplied by 2]

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""
name = input("Enter your name: ")
age_str = input("Enter your age: ") 
favorite_number_str = input("Enter your favorite number: ")
age = int(age_str)
favorite_number = int(favorite_number_str)
age_in_10_years = age + 10
doubled_favorite = favorite_number * 2
print("Hello " + name + "!")
print("In 10 years, you'll be " + str(age_in_10_years) + " years old.")
print("Your favorite number doubled is " + str(doubled_favorite) + ".")


""""
PROBLEM 2: [Grade Calculator]

Write a program that takes a numerical grade (0-100) and converts it to a letter grade:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F

Also include a message for each grade range.
"""
grade = int(input("Enter your grade: "))
if grade >= 90:
    letter = "A"
    message = "Great work! Keep it up!"
elif grade >= 80:
    letter = "B"
    message = "Could do better"
elif grade >= 70:
    letter = "C"
    message = "Its alright"
elif grade >= 60:
    letter = "D"
    message = "Study more."
else:
    letter = "F"
    message = "Turn in your work."
print(f"Your grade is an {letter}. {message}")


"PROBLEM 3: [Number Pattern Counter]"
"""Will count up replacing multiples of 3 with FIZZ and will count backwards with your number"""

num = int(input("Enter a number: "))

print("Pattern 1 (counting up with Fizz):")
for i in range(1, num + 1):
    if i % 3 == 0:
        print("Fizz", end=" ")
    else:
        print(i, end=" ")

print("\n\nPattern 2 (even numbers counting down):")
current = num
while current >= 0:
    if current % 2 == 0:
        print(current, end=" ")
    current -= 1




# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")


print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here


