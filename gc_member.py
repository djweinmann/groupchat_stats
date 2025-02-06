# class to represent member of a group_chat
class Member:

    # initialize a user with a name and list of participants
    def __init__(self, name, participants):
        self.name = name
        self.message_count = 0
        self.reaction_received_count = 0
        self.reaction_given_count = 0
        self.reaction_from_member = {participant['name']: 0 for participant in participants}
        self.reaction_to_member = {participant['name']: 0 for participant in participants}

    # increment message count
    def increment_message_count(self):
        self.message_count += 1

    # increment reaction received count
    def increment_reaction_received_count(self):
        self.reaction_received_count += 1

    # increment reaction given count
    def increment_reaction_given_count(self):
        self.reaction_given_count += 1

    # increment reaction from member count for given reactor
    def increment_reaction_from_member(self, reactor):
        self.reaction_from_member[reactor] += 1

    # increment reaction to member count for given sender
    def increment_reaction_to_member(self, sender):
        self.reaction_to_member[sender] += 1

    # return name of member
    def get_name(self):
        return self.name

    # return message count of member
    def get_message_count(self):
        return self.message_count

    # return reaction count of member
    def get_reaction_received_count(self):
        return self.reaction_received_count
    
    # return reaction count of member
    def get_reaction_given_count(self):
        return self.reaction_given_count

    # get the ratio of reactions received to messages sent
    def get_reactions_per_message(self):
        if self.get_message_count() == 0:
            return 0
        else:
            return self.get_reaction_received_count() / self.get_message_count()

    # get the message to reaction ratio of a user
    def get_messages_per_reaction(self):
        if self.get_reaction_received_count() == 0:
            return 0
        else:
            return self.get_message_count() / self.get_reaction_received_count()
    
    # get the total reactions from member of given name
    def get_reactions_from_member(self, name):
        return self.reaction_from_member[name]

    # get the total reactions to member of given name
    def get_reactions_to_member(self, name):
        return self.reaction_to_member[name]
    
    # get the ratio of reactions received to messages sent
    def get_reactions_per_message(self):
        if self.get_message_count() == 0:
            return 0
        else:
            return self.get_reaction_received_count() / self.get_message_count()