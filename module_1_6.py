# phone_book = {'Denis': 88005553535, 'Max': 88005553534}
# phone_book['Denis'] = 1234567890
# phone_book['Anton'] = 987654321
# # del phone_book ['Max']
# phone_book.update({'Sasha': 867564453534,
#                    'Alex': 6564563343647})
# print(phone_book.get('Max'))
# print(phone_book)

# set_ = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', True, (1, 2, 3)}
# list_ = [1, 1, 1, 1, 2, 3, 2, 2]
# print(set(list_))

my_dict = {'Vasya': 1991, 'Fedya': 1989, 'Olga': 1996}
print(my_dict)
print(my_dict.get('Olga'))
print(my_dict.get('Petya'))
my_dict.update({'Katya': 1993,
               'Andrei': 1991})
print(my_dict)
a = my_dict.pop('Fedya')
print(a)
print(my_dict)

my_set = {9, 9, 'Privet', 8, 6, 'Voda', 8, 4, 'Privet', True}
print(my_set)
my_set.add(5)
my_set.add('Monkey')
my_set.update([(1, 2, 3), 'Time'])
my_set.discard('Voda')
print(my_set)