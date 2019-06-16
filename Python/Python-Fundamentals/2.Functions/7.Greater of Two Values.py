def greater(data_type, value1, value2):
    if data_type == "int":
        if int(value1) >= int(value2):
            print(value1)
        elif int(value2) > int(value1):               # equal to else in this case
            print(value2)

    elif data_type == "char":
        is_greater = ord(value1) >= ord(value2)
        if is_greater:
            print(value1)
        elif not is_greater:                          # equal to else in this case
            print(value2)

    elif data_type == "string" and value1 >= value2:  # compares every letter (char) of the string
        print(value1)
    elif data_type == "string" and value1 < value2:
        print(value2)


greater(input(), input(), input())
