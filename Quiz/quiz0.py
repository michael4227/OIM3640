"""
Question 1:
Write a function that prompts the user for a weight on earth and prints the equivalent weight on the moon (16.5%)
Weight on Moon = weight on Earth * 0.165
Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
"""
# weight_on_earth = float(input('Please enter your weight on earth in kg:'))
# weight_on_earth = float(weight_on_earth)
# weight_on_moon = weight_on_earth*0.165
# print(f'Your weight on moon is {weight_on_moon} kg')
'''
Question 2:

Write a function that takes two arguments - 1. weight on earth (float), 2. planet (str) - and returns the equivalent weight on that planet. We assume Moon is a planet although it is not.

Weight on Moon = weight on Earth * 0.165
Weight on Mars = weight on Earth * 0.378
Weight on Jupiter = weight on Earth * 2.528

Notice:
1. Please write pseudo-code before coding the function.
2. Your function should include docstring.
3. Write your own test code, i.e. call the function.
'''

# 1. ask for user's weight
# 2. ask for the planet
# 3. calculation
# 4. print the weight on the corresponding planet


# weight_on_earth = float(input('Please enter your weight on earth in kg:'))
# planet = input('Please enter your planet:')
# '''asking for the user's inputs'''
# def weight_on_planet(weight_on_earth,planet):
#     if planet is 'moon':
#         weight_on_moon = weight_on_earth*0.165
#         print(f'Your weight on moon is {weight_on_moon} kg')
#     if planet is 'mars':
#         weight_on_mars = weight_on_earth * 0.378
#         print(f'Your weight on mars is {weight_on_mars} kg')
#     if planet is 'jupiter':
#         weight_on_jupiter = weight_on_earth * 2.528
#         print(f'Your weight on jupiter is {weight_on_jupiter} kg')
#     else:
#         print('Sorry, I do not know this planet.')
# print(weight_on_planet(weight_on_earth,planet))
# """call function"""

# V2
# docstring should be after the def, instead of in front of it
def weight_on_planet(weight_on_earth,planet):
    '''the outcome unit would be the same as your input unit'''
    # weight_on_earth = float(input('Please enter your weight on earth in kg:'))
    # planet = input('Please enter your planet:')
    # weight_on_earth = float(weight_on_earth)
    if planet == 'moon':
        weight_on_moon = weight_on_earth*0.165
        return (f'Your weight on moon is {weight_on_moon} kg')
    if planet == 'mars':
        weight_on_mars = weight_on_earth * 0.378
        return (f'Your weight on mars is {weight_on_mars} kg')
    if planet == 'jupiter':
        weight_on_jupiter = weight_on_earth * 2.528
        return (f'Your weight on jupiter is {weight_on_jupiter} kg')
    else:
        return ('Sorry, I do not know this planet.')
print(weight_on_planet(80,'mars'))
# return 怎么用