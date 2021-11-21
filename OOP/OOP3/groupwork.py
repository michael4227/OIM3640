# from collections import Counter
class Recipe:
    """
    Categorizes Food
    """
    def __init__(self, country, time, ingredients):
        self.country = country
        self.time = time
        self.ingredients = ingredients

    def __str__(self):
        new_str = ''
        for ingredient, quantity in self.ingredients.items():
            new_str += f'\n\t{ingredient}: {quantity} gram/units'
        return f'The dish is from {self.country} and takes {self.time} minutes to cook. There are {new_str} in the recipe.'

    def __eq__(self, another):
        """
        Lets you know if its from the same culture.
        """
        return self.country == another.country

    def make_sweeter(self): 
        """
        Adds more sugar to a sweet recipe
        """
        for ingredient, quantity in self.ingredients.items():
            if 'sugar' in ingredient:
                self.ingredients["sugar"] = quantity + 5
            else:
                print("This is dish is not supposed to be sweet!")
        return (self.ingredients)

        # if 'sugar' in self.ingredients.key:
                #     print('Do not add anymore sugar!')
                # else:
                #     self.ingredients["sugar"]: 5

    def combine_soup(self, another):
        """
        combines two ingredients lists.
        """
        # self = Counter(self.ingredients)
        # another = Counter(another.ingredients)
        # good_soup = self + another
        for ingredient, quantity in self.ingredients.items():
            if ingredient in another.ingredients:
                self.ingredients[ingredient] = quantity + another.ingredients[ingredient]
        for ingredient, quantity in another.ingredients.items():
            if ingredient not in self.ingredients:
                self.ingredients[ingredient] = quantity
        return(self.ingredients)

        

        
tomato_soup = Recipe("Spain", 30, {"tomatoes": 3, "basil": 1, "cream": 2, "sugar":2, "carrots": 1})
cabbage_soup = Recipe("Russia", 120, {"cabbage": 1, "carrots": 1, "potatoes": 3, "butter": 1})


# Test Code
# print(tomato_soup==cabbage_soup)
# Expect "False"

# print(Recipe.combine_soup(tomato_soup,cabbage_soup))
# Expect "{'tomatoes': 3, 'basil': 1, 'cream': 2, 'sugar': 2, 'cabbage': 1, 'carrots': 2, 'potatoes': 3, 'butter': 1}"


# print(Recipe.make_sweeter(tomato_soup))
# Expect "{'tomatoes': 3, 'basil': 1, 'cream': 2, 'sugar': 7}"