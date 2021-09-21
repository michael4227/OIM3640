"""
Question 1:
Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)
Weight on Moon = weight on Earth * 0.165
Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""
weight_on_earth = input('Please enter your weight on earth in kg:')
weight_on_earth = float(weight_on_earth)
weight_on_moon = weight_on_earth*0.165
print(f'Your weight on moon is {weight_on_moon} kg')