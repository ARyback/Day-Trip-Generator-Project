import random

destination_list = ['Milwaukee', 'Chicago', 'Wausau', 'Green Bay', 'Minneapolis']
restaurant_list = ['Calderone Club', 'County Clare', 'Crafty Cow', 'BBQ City' , 'Cada de Alberto']
transportation_list = ['Car', 'Plane', 'Train', 'Truck', 'Motorcycle']
entertainment_list = ['Jimmy Buffett Concert', 'Football Game', 'Museum Tour', 'Comedy Show', 'Brewery Tour']

total_list = [[destination_list], [restaurant_list], [transportation_list], [entertainment_list]]

choose_initial = input(f"Do you like the initial trip we picked for you? y or n: ")

def initial_option(option_list):
    rand_option = option_list[random.randint(0, 4)]
    return rand_option

def initial_trip():
    initial_destination = initial_option(destination_list)
    initial_restaurant = initial_option(restaurant_list)
    initial_transportation = initial_option(transportation_list)
    initial_entertainment = initial_option(entertainment_list)
    print(f"Congratulations on choosing {initial_destination} as your destination, {initial_restaurant} as your restaurant, {initial_transportation} as your transportation, and {initial_entertainment} as your entertainment.")  



def option_generator(option_list, activity):
    while True:
        rand_option = option_list[random.randint(0, 4)]
        input_choice = input(f'We have selected {rand_option} as your {activity}! Do you like it? Enter y or n: ')
        if input_choice == 'y':
            print(f'Congratulations on choosing {rand_option} as your {activity}! Let us move on')
            return rand_option
            break

def day_trip_generator():
    initial_trip()
    choose_initial
    if choose_initial == "n":
        destination_generator = option_generator(destination_list, "destination")
        restaurant_generator = option_generator(restaurant_list, "restaurant")
        transportation_generator = option_generator(transportation_list, "mode of transportation")
        entertainment_generator = option_generator(entertainment_list, "entertainment")
        print(f"Congratulations on choosing {destination_generator} as your destination, {restaurant_generator} as your restaurant, {transportation_generator} as your transportation, and {entertainment_generator} as your entertainment.")
    
day_trip_generator()



