import random

destination_list = ["Milwaukee", "Chicago", "Wausau", "Green Bay", "Minneapolis"]
restaurant_list = ["Calderone Club", "County Clare", "Crafty Cow", "BBQ City", "Cada de Alberto"]
transportation_list = ["Car", "Plane", "Train", "Truck", "Motorcycle"]
entertainment_list = ["Jimmy Buffett Concert", "Football Game", "Museum Tour", "Comedy Show", "Brewery Tour"]

def option(list_option):
    return list_option[random.randint(0, len(list_option) - 1)]

destination_option = option(destination_list)
restaurant_option = option(restaurant_list)
transportation_option = option(transportation_list)
entertainment_option = option(entertainment_list)

def initial_trip():
    print(f"Congratulations on choosing {destination_option} as your destination, {restaurant_option} as your restaurant, {transportation_option} as your transportation, and {entertainment_option} as your entertainment.")  

def initial_congrats():
    print("Great! Have fun on your trip. Be sure to work with us again!")

def trip_final(destination, restaurant, transportation, entertainment):
    print(f"Congratulations on finalizing your trip to {destination}! It will be great dining at {restaurant} as your restaurant! You are going to enjoy traveling by {transportation}. But you will especially love {entertainment}.")

def option_generator(option_list, activity):
    while True:
        rand_option = option_list[random.randint(0, len(option_list) - 1)]
        input_choice = input(f"We have selected {rand_option} as your {activity}! Do you like it? Enter y or n: ")
        if input_choice == "y":
            print(f"Congratulations on choosing {rand_option} as your {activity}! Let us move on")
            return rand_option
            break

def day_trip_generator():
    initial_trip()
    choose_initial = input(f"Do you like the initial trip we picked for you? y or n: ")
    if choose_initial == "y":
        initial_congrats()
    else:
        destination_generator = option_generator(destination_list, "destination")
        restaurant_generator = option_generator(restaurant_list, "restaurant")
        transportation_generator = option_generator(transportation_list, "mode of transportation")
        entertainment_generator = option_generator(entertainment_list, "entertainment")
        trip_final(destination_generator, restaurant_generator, transportation_generator, entertainment_generator)

day_trip_generator()




