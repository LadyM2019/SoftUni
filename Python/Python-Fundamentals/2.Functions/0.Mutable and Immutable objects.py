# https://www.dataquest.io/blog/tutorial-functions-modify-lists-dictionaries-python/  - MUST SEE
# https://www.bogotobogo.com/python/python_functions_def.php


def fun(x, y, z):
    x = z - y
    y = z - 1
    print(x, y, z)


a = 2
b = 4
c = 8
fun(a, b, b + c)
print(a, b, c)          # The initial values of a, b and c are unchanged
