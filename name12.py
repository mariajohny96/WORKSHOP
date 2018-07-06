dictionary = {'george' : 16, 'amber' : 19}
search_age = raw_input("Provide age")
for age in dictionary.values():
    if age == search_age:
        name = dictionary[age]
        print name
