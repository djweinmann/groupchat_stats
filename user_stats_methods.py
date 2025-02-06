import time
import json
from misc_methods import *
# handle and prompt user stats inputs
def user_stats_input(json_file_names, members):
    
    # print number next to users and add to valid input list
    valid_user_inputs = ['b']
    count = 1
    for mem in members:
        valid_user_inputs.append(str(count))
        count += 1

    # variable to break loop
    running = True
    while running:

        # blank row
        print('')

        # prompt and handle user stats input
        print('What user would you like to get stats for?')
        i = 1
        while i < count:
            print(str(i) + ' - ' + members[i - 1].get_name())
            i += 1
        print('b - back')
        print('')

        # get input
        user_input = input()

        # handle b input
        if user_input == 'b':
            return

        # handle invalid input
        if user_input not in valid_user_inputs:
            print('')
            print('Invalid input, try again')

        # handle user number input
        if user_input in valid_user_inputs:
            stat_for_member(json_file_names, members, members[int(user_input) - 1])


# show stats for specific member
def stat_for_member(json_file_names, members, member):

    # blank row
    print('')

    # display base stats
    print(member.get_name() + ' has...')
    print('sent ' + str(member.get_message_count()) + ' messages')
    print('recieved ' + str(member.get_reaction_received_count()) + ' reactions')
    print('given ' + str(member.get_reaction_given_count()) + ' reactions') 

    # variable to break loop
    running = True
    while running:
        
        # blank row
        print('')

        # valid user inputs
        valid_user_inputs = ['1', '2', '3', '4', '5', '6', 'b']

        # prompt user inputs
        print('What additional stats would you like to get for ' + member.get_name() + '?')
        print('1 - reactions received per message')
        print('2 - reactions from groupchat member')
        print('3 - reactions to groupchat member')
        print('4 - total messages by hour')
        print('5 - total messages by month')
        print('6 - percentage of messages with X or more likes')
        print('b - back')
        print('')

        # get user input
        user_input = input()

        # handle b input
        if user_input == 'b':
            return

        # handle 1 input
        if user_input == '1':
            print('')
            print(member.get_name() + ' has received ' + str(round(member.get_reactions_per_message(), 4)) + ' reactions per message sent')

        # handle 2 input
        if user_input == '2':
            reactions_from_member(member, members)

        # handle 3 input
        if user_input == '3':
            reactions_to_member(member, members)

        # handle 4 input
        if user_input == '4':
            user_messages_by_hour(member, json_file_names)

        # handle 5 input
        if user_input == '5':
            user_messages_by_month(member, json_file_names)

        # handle 6 input
        if user_input == '6':
            user_messages_x_likes(member, json_file_names)

        # handle invalid input
        if user_input not in valid_user_inputs:
            print('')
            print('Invalid input, try again')


# get input for and display reactions from specific member
def reactions_from_member(member, members):

    # print number next to users and add to valid input list
    valid_user_inputs = ['b']
    count = 1
    for mem in members:
        valid_user_inputs.append(str(count))
        count += 1

    # variable to break loop
    running = True
    while running:

        # blank row
        print('')

        # prompt and handle user stats input
        print('What user would you like to get reactions from?')
        i = 1
        while i < count:
            print(str(i) + ' - ' + members[i - 1].get_name())
            i += 1
        print('b - back')
        print('')

        # get input
        user_input = input()

        # handle b input
        if user_input == 'b':
            return

        # handle invalid input
        if user_input not in valid_user_inputs:
            print('')
            print('Invalid input, try again')

        else:
            running = False

            # print results
            print('')
            print(member.get_name() + ' has received ' + 
                  str(member.get_reactions_from_member(members[int(user_input) - 1].get_name())) + 
                  ' reactions from ' + members[int(user_input) - 1].get_name())


# get input for and display reactions from specific member
def reactions_to_member(member, members):

    # print number next to users and add to valid input list
    valid_user_inputs = ['b']
    count = 1
    for mem in members:
        valid_user_inputs.append(str(count))
        count += 1

    # variable to break loop
    running = True
    while running:

        # blank row
        print('')

        # prompt and handle user stats input
        print('What user would you like to get reacions to?')
        i = 1
        while i < count:
            print(str(i) + ' - ' + members[i - 1].get_name())
            i += 1
        print('b - back')
        print('')

        # get input
        user_input = input()

        # handle b input
        if user_input == 'b':
            return

        # handle invalid input
        if user_input not in valid_user_inputs:
            print('')
            print('Invalid input, try again')

        else:
            running = False

            # print results
            print('')
            print(member.get_name() + ' has given ' + 
                  str(member.get_reactions_to_member(members[int(user_input) - 1].get_name())) + 
                  ' reactions to ' + members[int(user_input) - 1].get_name())
            

# print messages next to each hour in local time
def user_messages_by_hour(member, json_file_names):

    # blank row
    print('')

    # initialize dictionary with each hour and corresponding messages
    hours_messages = dict.fromkeys(range(24), 0)

    # iterate through every file provided
    for file_name in json_file_names:

        # open file and load with json
        with open('message_files\\' + file_name) as file:
            doc = json.load(file)

        # iterate through every message to increment message count for corresponding hour
        messages = doc['messages']
        for message in messages:

            timestamp = int(str(message['timestamp_ms'])[:-3])

            # check if message sender is same as member finding stats for
            if message['sender_name'] == member.get_name():

                # check if it is a message like notification
                if 'content' in message:
                    
                    if message['content'].find(' liked a message') == -1:
                        
                        hours_messages[time.localtime(timestamp)[3]] += 1
    
    # print results
    print('hour (local time) : messages')
    print('-' * 28)

    i = 0
    for k, v in hours_messages.items():

        # buffer for formatting
        buf = ''
        if i < 10:
            buf = ' ' * 16
        else:
            buf = ' ' * 15
        
        i += 1

        print(str(k) +  buf + " : " + str(v))


# print messages per month next to each month
def user_messages_by_month(member, json_file_names):

    # blank row
    print('')

    # initialize dictionary with each hour and corresponding messages
    months_messages = {'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'May': 0, 'Jun': 0,
                      'Jul': 0, 'Aug': 0, 'Sep': 0, 'Oct': 0, 'Nov': 0, 'Dec': 0}

    # iterate through every file provided
    for file_name in json_file_names:

        # open file and load with json
        with open('message_files\\' + file_name) as file:
            doc = json.load(file)

        # iterate through every message to increment message count for corresponding hour
        messages = doc['messages']
        for message in messages:

            timestamp = int(str(message['timestamp_ms'])[:-3])

            # check if message sender is same as member finding stats for
            if message['sender_name'] == member.get_name():

                # check if it is a message like notification
                if 'content' in message:
                    
                    if message['content'].find(' liked a message') == -1:
                        
                        months_messages[int_to_month(time.localtime(timestamp)[1])] += 1
    
    # print results
    print('month : messages')
    print('-' * 16)

    for k, v in months_messages.items():
        print(str(k) +  "   : " + str(v))


# print the percentage of messages from a user with X or more likes
def user_messages_x_likes(member, json_file_names):

    # variable to break loop
    running = True
    while running:

        # blank row
        print('')

        # prompt and handle user input
        print('What minumum threshold of reactions would you like to see the percentage for?')
        print('')

        # get input
        user_input = input()

        # handle input, whether valid or invalid
        try:
            int(user_input)
        except:
            print('')
            print('Invalid input, try again')
        else:
            running = False
            like_dict = user_messages_x_dict(member, json_file_names)
            percentage = round(100 * dictionary_key_ratio(like_dict, int(user_input)), 2)
            print(member.get_name() + ' receives ' + user_input + ' or more reactions on ' +
                  str(percentage) + f'% of their messages')


# returns a dictionary with reaction count as key and total messages with that count as value
def user_messages_x_dict(member, json_file_names):

    # blank row
    print('')

    like_dict = {0: 0}

    # iterate through every file provided
    for file_name in json_file_names:

        # open file and load with json
        with open('message_files\\' + file_name) as file:
            doc = json.load(file)

        # iterate through every message to increment message count for corresponding reaction count
        messages = doc['messages']
        for message in messages:

            # check if message is from desired user
            if message['sender_name'] == member.get_name():

                # ensures message has content
                if 'content' in message:
                    if message['content'].find(' liked a message') == -1:

                        # check if message has reactions
                        if 'reactions' in message:

                            # get count of reactions
                            reaction_count = len(message['reactions'])

                            # increase dictionary count for corresponding key or creates it if doesn't yet exist
                            if reaction_count in like_dict.keys():
                                like_dict[len(message['reactions'])] += 1
                            else:
                                like_dict[reaction_count] = 1
                                
                        else:
                            like_dict[0] += 1

            else:
                # check if message has reactions
                        if 'reactions' in message:

                            # get count of reactions
                            reaction_count = len(message['reactions'])

                            # increase dictionary count for corresponding key or creates it if doesn't yet exist
                            if reaction_count in like_dict.keys():
                                like_dict[len(message['reactions'])] += 1
                            else:
                                like_dict[reaction_count] = 1
                                
                        else:
                            like_dict[0] += 1

    return like_dict