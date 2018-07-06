dict1= {}
for i in range(0,5):
	name=raw_input("Enter the name:")
	number= input("Enter the number:")
	dict1[name]= number
print dict1
search_number = input("Provide number: ")
for number in dict1.values():
    if number == search_number:
        name = dict1[number]
	 print name



