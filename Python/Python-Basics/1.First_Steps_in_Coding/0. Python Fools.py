"""Some Python Fools"""
a = ''
b = ' '  # the only value
c = None
d = []
e = 0
# False also has no value -> if condition evaluates to False

if a:  # When you write if variable(no matter which), the check will tell you if it exists or it is True
    print("print a ", a)

if b:
    print("print b ", b)

if c:
    print("print c ", c)

if d:
    print("print d ", d)

if e:
    print("print e ", e)

randomList = [1, 'a', 0, True, False, '', '0']
filteredList = list(filter(None, randomList))  # should be casted to a list!
print('The filtered elements are:', filteredList)       # Contains only the True values (the None values are filtered)

# When we loop through the final filteredList, we get the elements which are true: 1, a, True and '0'
# ('0' as a string is also true).
