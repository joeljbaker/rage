import itertools

''' May 2018 Challenge.

run print_solution() to solve the puzzle

Puzzle:
Jack has positive integer number of kids.
Their ages are all positive integers.
Their ages add up to Jack's desk number.
Ages multiple together to Jack's age.

Jill knows Jack's desk number.
If Jill knew Jack's age and number of kids she still couldn't work out the ages of the children.
Jill works out Jack's age.

What is the Jack's desk number?

'''

def print_solution():
    ''' helper method to run the code '''
    find_desk_num(family_scenarios(max_age=18, max_kids=6))

def find_desk_num(scenarios):
    ''' Determine Jack's desk number, if possible, based on the provided scenarios of children's ages.
    We are looking for the desk number that relates to:
      - the unique value of Jack's age for which Jill cannot know the ages of the children just by knowing the num_kids.
        ie: the unique value for Jack's age for which there are multiple permutations of children's ages for the same (jack_age, num_kids) combo '''

    # first, group each of the family scenarios by the desk number implied by each set of children's ages
    # and, inside this desk grouping, collect the different scenarios for each combination of jack's age and num_kids
    deskmap = build_deskmap(scenarios)

    # Jill knows that Jack's Age and number of kids does not uniquely identify the ages of his kids
    # So we look for a combination of jack_age and num_kids that has more than one permutation of different children's ages
    possible_outcomes = {}
    for desk_num, val in deskmap.iteritems():
        for (jack_age, num_kids), kids_ages_list in val.iteritems():
            if(len(kids_ages_list)>1):
                possible_outcomes[desk_num] = possible_outcomes.get(desk_num,[])
                possible_outcomes[desk_num].append(jack_age)

    # Jill knows Jack's desk number and is now able to work out Jack's age
    # So there must be a desk number for which there is only one value of Jack's age, that has, as above, enough permutations of children's ages to cause confusion!
    for desk_num, ages in possible_outcomes.iteritems():
        if(len(ages)==1):
            print "Desk num %i for Jack's age of %i" % (desk_num, ages[0])


def family_scenarios(max_age=18, max_kids=5):
    ''' generate a list of all unique permutations of children's ages.
        eg: (1,2) is a family of two children, aged 1 and 2
        max_age: oldest age of a child
        max_kids: largest family size
    '''

    kids = []
    for num_kids in range(1, max_kids+1):
        # sort each tuple and then convert to set so that [(1,2), (2,1)] is just represented once
        # may well be an option in itertools to handle the nCr uniqueness. who knows?
        # also would be nice to preserve the original ordering whilst removing the duplicates
        kids.extend(set([tuple(sorted(a)) for a in itertools.product(range(1, max_age+1), repeat=num_kids)]))
    return kids

def build_deskmap(scenarios):
    ''' build a dict, keyed by desk_num. values are another dict (ick). 
    the inner dict is keyed by the (jack_age, num_kids) combination, and values are all permutations for this combination '''

    deskmap = {}
    for kids_ages in scenarios:
        desk_num = sum(kids_ages)
        num_kids = len(kids_ages)
        jack_age = _calc_age(kids_ages)
        if jack_age > 117:  # oldest person in the world is currently 117. Oldest father is 94 or something...
            continue
        val = (jack_age, num_kids)

        deskmap[desk_num] = deskmap.get(desk_num, {})
        deskmap[desk_num][val] = deskmap[desk_num].get(val, [])
        deskmap[desk_num][val].append(kids_ages)
    return deskmap

def _calc_age(kids):
    ''' Jack's age is the product of his children's ages. Obviously '''

    jack_age  = 1
    for age in kids:
        jack_age = jack_age * age
    return jack_age

if __name__ == '__main__':
    print_solution()