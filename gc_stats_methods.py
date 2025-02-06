import time
import json
from misc_methods import *

# handle input for what gc stat to get
def gc_stats_input(json_file_names, members):

    # variable to break loop
    running = True
    while running:

        # blank row
        print('')

        # valid user inputs
        valid_user_inputs = ['1', '2', '3', '4', '5', '6', '7', 'b']

        # prompt and handle user input
        print('What groupchat stat would you like to get?')
        print('1 - reactions per message by member')
        print('2 - total messages by member')
        print('3 - total reactions given by member')
        print('4 - total reactions received by member')
        print('5 - total messages by hour')
        print('6 - total messages by month')
        print('7 - average message length by member')
        print('b - back')
        print('')

        # get input
        user_input = input()
        
        # handle b input
        if user_input == 'b':
            return
        
        # handle 1 input
        if user_input == '1':
            reactions_per_message_by_member(members)
        
        # handle 2 input
        if user_input == '2':
            messages_by_member(members)

        # handle 3 input
        if user_input == '3':
            reactions_received_by_member(members)

        # handle 4 input
        if user_input == '4':
            reactions_given_by_member(members)

        # handle 5 input
        if user_input == '5':
            total_messages_by_hour(members, json_file_names)

        # handle 6 input
        if user_input == '6':
            total_messages_by_month(members, json_file_names)

        # handle 7 input
        if user_input == '7':
            message_length_by_member(members, json_file_names)
            
        # handle invalid input
        if user_input not in valid_user_inputs:
            print('')
            print('Invalid input, try again')


# print name next to reactions per message for each member
def reactions_per_message_by_member(members):

    # blank row
    print('')
            
    # sort members from most to least reactions per message
    sorted_members = sorted(members, key = lambda x: x.get_reactions_per_message(), reverse=True)

    # get longest name
    longest = max_member_name_length(members)

    buf1 = ' ' * (longest - 6)
    buf2 = ' ' * (longest - 7)

    print('member' + buf1 + ' : reactions per message')
    print('-' * (24 + longest))

    # variables to hold totals
    total_messages = 0
    total_reactions = 0

    # print each member next to their reactions per message
    for mem in sorted_members:

        # increment totals
        total_messages += mem.get_message_count()
        total_reactions += mem.get_reaction_received_count()
                
        # buffer of spaces based on max name length
        buffer = ' ' * (longest - len(mem.get_name()))

        print(mem.get_name() + buffer + ' : ' + str(round(mem.get_reactions_per_message(), 4)))

    # print total
    print('-' * (24 + longest))
    if total_messages == 0:
        print('0')
    else:
        print('average' + buf2 + ' : ' + str(round(total_reactions / total_messages, 2)))


# print name next to messages sent for each member
def messages_by_member(members):

    # blank row
    print('')
            
    # sort members from most to least messages
    sorted_members = sorted(members, key = lambda x: x.get_message_count(), reverse=True)

    # get longest name
    longest = max_member_name_length(members)

    buf1 = ' ' * (longest - 6)
    buf2 = ' ' * (longest - 5)

    print('member' + buf1 + ' : messages sent')
    print('-' * (16 + longest))

    # variable to hold total
    total_messages = 0

    # print each member next to their message count
    for mem in sorted_members:

        # increment total
        total_messages += mem.get_message_count()

        # buffer of spaces based on max name length
        buffer = ' ' * (longest - len(mem.get_name()))

        print(mem.get_name() + buffer + ' : ' + str(mem.get_message_count()))

    # print total
    print('-' * (16 + longest))
    print('total' + buf2 + ' : ' + str(total_messages))


# print name next to total reactions received for each member
def reactions_received_by_member(members):

    # blank row
    print('')
            
    # sort members from most to least reactions received
    sorted_members = sorted(members, key = lambda x: x.get_reaction_received_count(), reverse=True)

    # get longest name
    longest = max_member_name_length(members)

    buf1 = ' ' * (longest - 6)
    buf2 = ' ' * (longest - 5)

    print('member' + buf1 + ' : reactions received')
    print('-' * (21 + longest))

    # variable to hold total
    total_reactions = 0

    # print each member next to their reaction received count
    for mem in sorted_members:

        # increment total
        total_reactions += mem.get_reaction_received_count()
                
        # buffer of spaces based on max name length
        buffer = ' ' * (longest - len(mem.get_name()))

        print(mem.get_name() + buffer + ' : ' + str(mem.get_reaction_received_count()))

    # print total
    print('-' * (21 + longest))
    print('total' + buf2 + ' : ' + str(total_reactions))


# print name next to total reactions given for each member
def reactions_given_by_member(members):

    # blank row
    print('')
            
    # sort members from most to least reactions given
    sorted_members = sorted(members, key = lambda x: x.get_reaction_given_count(), reverse=True)

    # get longest name
    longest = max_member_name_length(members)

    buf1 = ' ' * (longest - 6)
    buf2 = ' ' * (longest - 5)

    print('member' + buf1 + ' : reactions given')
    print('-' * (18 + longest))

    # variable to hold total
    total_reactions = 0

    # print each member next to their reaction given count
    for mem in sorted_members:

        # increment total
        total_reactions += mem.get_reaction_given_count()
                
        # buffer of spaces based on max name length
        buffer = ' ' * (longest - len(mem.get_name()))

        print(mem.get_name() + buffer + ' : ' + str(mem.get_reaction_given_count()))

    # print total
    print('-' * (18 + longest))
    print('total' + buf2 + ' : ' + str(total_reactions))


# print messages next to each hour in local time
def total_messages_by_hour(members, json_file_names):

    # blank row
    print('')

    # initialize dictionary with each hour and corresponding messages
    hours_messages = dict.fromkeys(range(24), 0)

    # list of names of members
    member_names = []
    for mem in members:
        member_names.append(mem.get_name())

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
            if message['sender_name'] in member_names:

                # check if it is a message like notification
                if 'content' in message:
                    if message['content'].find(' liked a message') == -1:
                        
                        hours_messages[time.localtime(timestamp)[3]] += 1

                else:
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
def total_messages_by_month(members, json_file_names):

    # blank row
    print('')

    # initialize dictionary with each hour and corresponding messages
    months_messages = {'Jan': 0, 'Feb': 0, 'Mar': 0, 'Apr': 0, 'May': 0, 'Jun': 0,
                      'Jul': 0, 'Aug': 0, 'Sep': 0, 'Oct': 0, 'Nov': 0, 'Dec': 0}
    
    # list of names of members
    member_names = []
    for mem in members:
        member_names.append(mem.get_name())

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
            if message['sender_name'] in member_names:

                # check if it is a message like notification
                if 'content' in message:
                    if message['content'].find(' liked a message') == -1:
                        
                        months_messages[int_to_month(time.localtime(timestamp)[1])] += 1

                else:
                    months_messages[int_to_month(time.localtime(timestamp)[1])] += 1
    
    # print results
    print('month : messages')
    print('-' * 16)

    for k, v in months_messages.items():
        print(str(k) +  "   : " + str(v))


# print average message length for each memebr of groupchat
def message_length_by_member(members, json_file_names):

    # blank row
    print('')

    # dictionary with key of each member name associated with total messages and total words per message
    message_lengths = {mem.get_name():[0, 0] for mem in members}

    # get longest name
    longest = max_member_name_length(members)

    buf = ' ' * (longest - 6)

    print('member' + buf + ' : characters per message')
    print('-' * (25 + longest))
    
    # iterate through every file provided
    for file_name in json_file_names:

        # open file and load with json
        with open('message_files\\' + file_name) as file:
            doc = json.load(file)

        # iterate through every message to increment message count for corresponding hour
        messages = doc['messages']
        for message in messages:

            # ensure message isn't like notification
            if 'content' in message:
                if message['content'].find(' liked a message') == -1:
                    
                    # ensure message is by member in current gc
                    if message['sender_name'] in message_lengths.keys():
                        
                        message_lengths[message['sender_name']][0] += 1
                        message_lengths[message['sender_name']][1] += len(message['content'])

    # order dict by average message length
    ordered_dict = sorted(message_lengths.items(), key = lambda x: second_over_first(x[1]), reverse=True)

    # print name next to average message length
    for k, v in ordered_dict:

        # buffer of spaces based on max name length
        buffer = ' ' * (longest - len(k))

        print(k + buffer + ' : ' + str(round(second_over_first(v), 2)))