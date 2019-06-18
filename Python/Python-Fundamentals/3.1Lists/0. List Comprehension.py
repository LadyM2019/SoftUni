lst = [1, 2, 3, 4, 5]
lst = ['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in lst]
print(lst)

# The ternary form of the if/else operator doesn't have an 'elif' built in,
# but you can simulate it in the 'else' condition:
for v in lst:
    if v == 1:
        print('yes')
    else:
        if v == 2:
            print('no')
        else:
            print('idle')
# So there's no direct 'elif' construct, but it can be simulated with nested if/else statements
'''
Key Points to Remember:
1.List comprehension is an elegant way to define and create lists based on existing lists.
2.List comprehension is generally more compact and faster than normal functions and loops for creating list.
3.However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
4.Remember, every list comprehension can be rewritten in for loop, 
but every for loop can’t be rewritten in the form of list comprehension.
5.List comprehensions DO NOT modify the list in-place
'''

# https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/
# https://www.pythonforbeginners.com/basics/list-comprehensions-in-python
# https://www.programiz.com/python-programming/list-comprehension
