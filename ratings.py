"""Restaurant rating lister."""

def creates_dictionary(filename):
    restaurant_dictionary = {}
    given_file = open(filename)
    for line in given_file:
        line = line.rstrip()
        words = line.split(":")
        restaurant_dictionary[words[0]] = words[1]
    return restaurant_dictionary


def prints_ratings_alphabetically(given_dictionary):
    restaurants = sorted(given_dictionary)
    for restaurant in restaurants:
        print(f"{restaurant} is rated at {given_dictionary[restaurant]}.")

restaurant_dictionary = creates_dictionary("scores.txt")

def asks_user_for_rating():
    user_restaurant = input("What restaurant would you like to rate? > ")
    user_ratings = input("What rating would you like to enter? > ")
    upgrade_dictionary(user_restaurant, user_ratings)
  
def upgrade_dictionary(restaurant_name, rating):
    if restaurant_name in restaurant_dictionary:
        restaurant_dictionary[restaurant_name] = rating
    else:
        restaurant_dictionary[restaurant_name] = rating



asks_user_for_rating()
prints_ratings_alphabetically(restaurant_dictionary)