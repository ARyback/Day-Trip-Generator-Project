print('Welcome to destination day trip generator! You came to the right place!')

import random

destination_list = ['Milwaukee', 'Chicago', 'Wausau', 'Green Bay', 'Minneapolis']
restaurant_list = ['Calderone Club', 'County Clare', 'Crafty Cow', 'BBQ City' , 'Cada de Alberto']
mode_of_transport = ['Car', 'Plane', 'Train', 'Truck', 'Motorcycle']
entertainment_list = ['Jimmy Buffett Concert', 'Football Game', 'Museum Tour', 'Comedy Show', 'Brewery Tour']

rand_destination = destination_list[random.randint(0, 4)]
rand_restaurant = restaurant_list[random.randint(0, 4)]
rand_transportation = mode_of_transport[random.randint(0, 4)]
rand_entertainment = entertainment_list[random.randint(0, 4)]

