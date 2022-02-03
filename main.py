print('Welcome to destination day trip generator! You came to the right place!')

import random

destination_list = ['Milwaukee', 'Chicago', 'Wausau', 'Green Bay', 'Minneapolis']
restaurant_list = ['Calderone Club', 'County Clare', 'Crafty Cow', 'BBQ City' , 'Cada de Alberto']
mode_of_transport = ['Car', 'Plane', 'Train', 'Truck', 'Motorcycle']
entertainment_list = ['Jimmy Buffett Concert', 'Football Game', 'Museum Tour', 'Comedy Show', 'Brewery Tour']

#rand_destination = destination_list[random.randint(0, 4)]
rand_restaurant = restaurant_list[random.randint(0, 4)]
rand_transportation = mode_of_transport[random.randint(0, 4)]
rand_entertainment = entertainment_list[random.randint(0, 4)]
user_dest = 'y'

while user_dest == 'y':
    rand_destination = destination_list[random.randint(0, 4)]
    destination_option = input(f'We have selected {rand_destination} as your city of choice! Do you like it? Enter y or n: ')
    if destination_option == 'y':
        print(f'Congratulations on choosing {rand_destination}! Let us move on')
    else:
        rand_destination = destination_list[random.randint(0, 4)]
        destination_option = input(f'We have selected {rand_destination} as your city of choice! How does this sound? Enter y or n: ')
        if user_dest == 'y':
            print(f'Congratulations on choosing {rand_destination}! Let us move on.')
            break
