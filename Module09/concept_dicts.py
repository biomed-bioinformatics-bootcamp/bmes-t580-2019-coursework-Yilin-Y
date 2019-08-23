# the Dictionaries can be used to store data by key
# it also provide the function of lookup
# just kind of an example for dictionaries dicts

lookup = {}
lookup = dict()
lookup = {'age': 42, 'loc': 'Italy'}
lookup = dict(age=42, loc='Italy')


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name


gandolf = Wizard("Gladolf", 42)
print(gandolf.__dict__)

print(lookup) # print the lookup
print(lookup['loc']) # print the location

lookup['cat'] = 'Fun code demos' # record the lookup key

if 'cat' in lookup:
    print(lookup['cat']) # used the lookup to find if cat is in lookup, once it find the key "cat", system wiil print 'Fun code demos'

# Suppose these came from a data source, e.g. database, web service, etc
# And we want to randomly access them
import collections # import the collections modules for data used

# format of users
User = collections.namedtuple('User', 'id, name, email')

# list of all users
users = [
    User(1, 'user1', 'user1@talkpython.fm'),
    User(2, 'user2', 'user2@talkpython.fm'),
    User(3, 'user3', 'user3@talkpython.fm'),
    User(4, 'user4', 'user4@talkpython.fm'),
]

lookup = dict()
for u in users:
    lookup[u.email] = u
# asking the system to find key with user4@talkpython.fm, and print as the format shows above, such as ('User', 'id, name, email')
print(lookup['user4@talkpython.fm'])


# LAMBDAS
def find_significant_numbers(nums, predicate):
    for n in nums:
        if predicate(n):
            yield n


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34]
sig = find_significant_numbers(numbers, lambda x: x % 2 == 1)
print(list(sig)) # asking to print the significant nuumbers what /2 will equal to 1 like odd number