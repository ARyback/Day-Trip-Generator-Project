
#     user_choice = 'n'
#     while user_choice == 'n':
#         rand_option = option_list[random.randint(0, 4)]
#         input_choice = input(f'We have selected {rand_option} as your choice! Do you like it? Enter y or n: ')
#         if input_choice == 'y':
#             print(f'Congratulations on choosing {rand_option}! Let us move on')
#             break

#         # else:
        #     rand_option = option_list[random.randint(0, 4)]
        #     input_choice = input(f'We have selected {rand_option} as your choice! How does this sound? Enter y or n: ')
        #     user_choice = input_choice
        #     if user_choice == 'y':
        #         print(f'Congratulations on choosing {rand_option}! Let us move on.')
        #         break
        #     else:
        #         rand_option = option_list[random.randint(0, 4)]
        #         input_choice = input(f'We have selected {rand_option} as your choice! How does this sound? Enter y or n: ')
        #         user_choice = rand_option
# user_dest = 'n'
# while user_dest == 'n':
#     rand_destination = destination_list[random.randint(0, 4)]
#     destination_option = input(f'We have selected {rand_destination} as your city of choice! Do you like it? Enter y or n: ')
#     if destination_option == 'y':
#         print(f'Congratulations on choosing {rand_destination}! Let us move on')
#         break
#     else:
#         rand_destination = destination_list[random.randint(0, 4)]
#         destination_option = input(f'We have selected {rand_destination} as your city of choice! How does this sound? Enter y or n: ')
#         user_dest = destination_option
#         if user_dest == 'y':
#             print(f'Congratulations on choosing {rand_destination}! Let us move on.')
#             break
#         else:
#             rand_destination = destination_list[random.randint(0, 4)]
#             destination_option = input(f'We have selected {rand_destination} as your city of choice! How does this sound? Enter y or n: ')
#             user_dest = destination_option


# user_rest = 'n'
# while user_rest == 'n':
#     rand_restaurant = restaurant_list[random.randint(0, 4)]
#     restaurant_option = input(f'We have selected {rand_restaurant} as your restaurant of choice! Do you like it? Enter y or n: ')
#     if restaurant_option == 'y':
#         print(f'Congratulations on choosing {rand_restaurant}! Let us move on')
#         break
#     else:
#         rand_restaurant = restaurant_list[random.randint(0, 4)]
#         restaurant_option = input(f'We have selected {rand_restaurant} as your restaurant of choice! How does this sound? Enter y or n: ')
#         if user_rest == 'y':
#             print(f'Congratulations on choosing {rand_restaurant}! Let us move on.')
#             break
#         else:
#             rand_restaurant = restaurant_list[random.randint(0, 4)]
#             restaurant_option = input(f'We have selected {rand_restaurant} as your city of choice! How does this sound? Enter y or n: ')
#             user_rest = restaurant_option

# user_transport = 'n'
# while user_transport == 'n':
#     rand_transportation = transportation_list[random.randint(0, 4)]
#     transportation_option = input(f'We have selected {rand_transportation} as your transportation of choice! Do you like it? Enter y or n: ')
#     if transportation_option == 'y':
#         print(f'Congratulations on choosing {rand_transportation}! Let us move on')
#         break
#     else:
#         rand_transportation = transportation_list[random.randint(0, 4)]
#         transportation_option = input(f'We have selected {rand_transportation} as your transportation of choice! How does this sound? Enter y or n: ')
#         if user_transport == 'y':
#             print(f'Congratulations on choosing {rand_transportation}! Let us move on.')
#             break
#         else:
#             rand_transportation = transportation_list[random.randint(0, 4)]
#             transportation_option = input(f'We have selected {rand_transportation} as your transportation of choice! How does this sound? Enter y or n: ')
#             user_transport = transportation_option

# user_ent = 'n'
# while user_ent == 'n':
#     rand_ent = entertainment_list[random.randint(0, 4)]
#     entertainment_option = input(f'We have selected {rand_ent} as your entertainment of choice! Do you like it? Enter y or n: ')
#     if entertainment_option == 'y':
#         print(f'Congratulations on choosing {rand_ent}! Let us move on')
#         break
#     else:
#         rand_ent = entertainment_list[random.randint(0, 4)]
#         entertainment_option = input(f'We have selected {rand_ent} as your entertainment of choice! How does this sound? Enter y or n: ')
#         if user_transport == 'y':
#             print(f'Congratulations on choosing {rand_ent}! Let us move on.')
#             break
#         else:
#             rand_ent = entertainment_list[random.randint(0, 4)]
#             entertainment_option = input(f'We have selected {rand_ent} as your entertainment of choice! How does this sound? Enter y or n: ')
#             user_ent = entertainment_option

# print(f'Congratulations on going to {rand_destination} via {rand_transportation} to eat at {rand_restaurant} and see {rand_ent}.')