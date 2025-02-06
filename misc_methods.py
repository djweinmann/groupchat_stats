# convert integer (1-12) to month
def int_to_month(num):
    if num == 1:
        return 'Jan'
    elif num == 2:
        return 'Feb'
    elif num == 3:
        return 'Mar'
    elif num == 4:
        return 'Apr'
    elif num == 5:
        return 'May'
    elif num == 6:
        return 'Jun'
    elif num == 7:
        return 'Jul'
    elif num == 8:
        return 'Aug'
    elif num == 9:
        return 'Sep'
    elif num == 10:
        return 'Oct'
    elif num == 11:
        return 'Nov'
    else:
        return 'Dec'


# find longest name in list of members
def max_member_name_length(members):

    # longest name
    longest = 0

    # iterate through members and update longest name
    for mem in members:
        longest = max(len(mem.get_name()), longest)

    return longest


# returns ratio from dict of total value of keys equal or larger than input relative to total value of all keys
def dictionary_key_ratio(dictionary, inp):
    
    larger = 0
    total = 0

    # iterate through dictionary
    for k, v in dictionary.items():

        # increment total of values with key >= input
        if k >= inp:
            larger += v

        # increment total of all values
        total += v
    
    return larger / total


# return value of second item in list divided by first item in list
def second_over_first(l):
    if l[0] == 0:
        return 0
    else:
        return l[1] / l[0]