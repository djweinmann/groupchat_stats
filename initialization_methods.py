import os
from gc_member import Member
from user_stats_methods import *
from gc_stats_methods import *
import json

# add all file names from message_files folder to provided list
def get_file_names(json_file_names):
    dir_path = 'message_files\\'
    for path in os.scandir(dir_path):
        if path.is_file() and '.gitignore' not in path.name:
            json_file_names.append(path.name)


# add all participant names from given file to provided list
def get_participant_names(json_file_name, members):

    # load file
    with open('message_files\\' + json_file_name) as file:
        doc = json.load(file)

    # add participants to list of mems
    participants = doc['participants']
    for participant in participants:
        members.append(Member(participant['name'], participants))


# add messages from list of file names to each member in list
def add_messages(message, members):

    # iterate through each member
    for mem in members:

        # check if sender name is same as member name
        if message['sender_name'] == mem.get_name():

            # check if it is a message like notification
            if 'content' in message:
                if message['content'].find(' liked a message') == -1:

                    # increment message count
                    mem.increment_message_count()

            else:

                # increment message count
                mem.increment_message_count()


# add reactions from list of file names to each member in list
def add_reactions(message, members):
    sender = message['sender_name']
    
    # check if message has reactions
    if 'reactions' in message:

        # iterate through reactions
        reactions = message['reactions']
        for reaction in reactions:
            reactor = reaction['actor']
                
            # iterate through each member
            for mem in members:

                # check if sender same is same as member name
                if sender == mem.get_name():

                    # increment reaction received count of member
                    mem.increment_reaction_received_count()

                    # checks if reactor is member and then increments reaction from member for the reactor
                    if reactor in mem.reaction_from_member.keys():
                        mem.increment_reaction_from_member(reactor)

                # check if reactor is same as member name
                if reactor == mem.get_name():
                    
                    # increament reaction given count of member
                    mem.increment_reaction_given_count()

                    if sender in mem.reaction_to_member.keys():
                        mem.increment_reaction_to_member(sender)



# fully given list of json file names, update each member in list
def update_members(json_file_names, members):

    # iterate through every given file name
    for file_name in json_file_names:

        # open file and load with json
        with open('message_files\\' + file_name) as file:
            doc = json.load(file)

        # iterate through every message to increment message count for each person
        messages = doc['messages']
        for message in messages:

            add_messages(message, members)
            add_reactions(message, members)


# handle user and prompt initial user inputs
def initial_input(json_file_names, members):
    
    # variable to break loop
    running = True
    while (running):

        # blank row
        print('')
        
        # prompt and handle initial input
        valid_initial_inputs = ['1', '2', 'x']
        print('What would you like to do?')
        print('1 - get user stats')
        print('2 - get groupchat stats')
        print('x - exit program')
        print('')

        # get input
        initial_input = input()

        # handle 1 input
        if initial_input == '1':
            user_stats_input(json_file_names, members)

        # handle 2 input
        if initial_input == '2':
            gc_stats_input(json_file_names, members)

        # handle x input
        if initial_input == 'x':
            running = False

        # handle invalid input
        if initial_input not in valid_initial_inputs:
            print('')
            print('Invalid input, try again')
