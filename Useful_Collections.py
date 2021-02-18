from collections import Counter, defaultdict
import datetime


# Returns a dictionary with count of each item in the list
Books = ['Algorithms', 'Statistics', 'Database', 'Networking', 'Algorithms', 'Database']
print(f'Count of Books : {Counter(Books)}')


# Allows to store default value for dictionary and returns them when a key not present in dictionary is requested
dictionary = defaultdict(lambda: 'Key Not Present', {1: 'Employee', 2: 'Users', 3: 'Staff'})
print(dictionary[4])

print(f' Today date is :  {datetime.date.today()}')

# creates time object
print(f' Today time is : {datetime.time(3,44,00)}')