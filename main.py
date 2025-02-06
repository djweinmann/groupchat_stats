from initialization_methods import *

def main():

    # all json files to be parsed
    json_file_names = []
    get_file_names(json_file_names)
    
    # add all groupchat participants to list of members
    members = []
    get_participant_names(json_file_names[0], members)

    # add messages and reactions to members
    update_members(json_file_names, members)


    # print logo
    print('')
    print("""   ____                                         _               _         ____    _             _           _ 
  / ___|  _ __    ___    _   _   _ __     ___  | |__     __ _  | |_      / ___|  | |_    __ _  | |_   ___  | |
 | |  _  | '__|  / _ \  | | | | | '_ \   / __| | '_ \   / _` | | __|     \___ \  | __|  / _` | | __| / __| | |
 | |_| | | |    | (_) | | |_| | | |_) | | (__  | | | | | (_| | | |_       ___) | | |_  | (_| | | |_  \__ \ |_|
  \____| |_|     \___/   \__,_| | .__/   \___| |_| |_|  \__,_|  \__|     |____/   \__|  \__,_|  \__| |___/ (_)
                                |_|                                                                           """)

    # handle and prompt user input
    initial_input(json_file_names, members)


if __name__ == '__main__':
    main()