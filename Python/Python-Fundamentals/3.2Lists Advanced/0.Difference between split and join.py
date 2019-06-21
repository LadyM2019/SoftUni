list_of_lines = ['Hello, here we are again.',
                 'No, like telling you.',
                 'We are multiple lines stored in a list.',
                 'And join() will convert us in a string.']
string1 = '\n'.join(list_of_lines)            # creates a string from an iterable and separate the elements by a given argument
string2 = string1.split('\n')                 # creates a list from a string and separate the elements by a given argument

print(string1)
print()
print(string2)
print()
print(*list_of_lines, sep='\n')               # Equivalent of join() is achieved by unpacking the list
print()

# ____________________________________________________________________________________
counts2 = {"Alex": "Mama_value", "Alex2": "Aya_value"}
print(' => '.join(counts2.values()))  	      # join works only with text/strings


alex = "lol"
print(', '.join(alex))         				  # be careful what you join
