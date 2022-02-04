import random

destination_list = ['Milwaukee', 'Chicago', 'Wausau', 'Green Bay', 'Minneapolis']
restaurant_list = ['Calderone Club', 'County Clare', 'Crafty Cow', 'BBQ City' , 'Cada de Alberto']
transportation_list = ['Car', 'Plane', 'Train', 'Truck', 'Motorcycle']
entertainment_list = ['Jimmy Buffett Concert', 'Football Game', 'Museum Tour', 'Comedy Show', 'Brewery Tour']

def welcome():
    print('Welcome to the day trip generator! You came to the right place!')

def option_generator(option_list, activity):
    while True:
        rand_option = option_list[random.randint(0, 4)]
        input_choice = input(f'We have selected {rand_option} as your {activity}! Do you like it? Enter y or n: ')
        if input_choice == 'y':
            print(f'Congratulations on choosing {rand_option} as your {activity}! Let us move on')
            return rand_option
            break

    

def day_trip_generator():
    welcome()
    destination_generator = option_generator(destination_list, "destination")
    restaurant_generator = option_generator(restaurant_list, "restaurant")
    transportation_generator = option_generator(transportation_list, "mode of transportation")
    entertainment_generator = option_generator(entertainment_list, "entertainment")
    print(f"Congratulations on choosing {destination_generator} as your destination, {restaurant_generator} as your restaurant, {transportation_generator} as your transportation, and {entertainment_generator} as your entertainment.")
    
day_trip_generator()



