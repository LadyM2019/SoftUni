def find_greater(value1, value2):
    is_greater = value1 > value2
    if is_greater:
        return value1
    elif not is_greater:                          # equal to else in this case
        return value2


def main():
    data_type = input()            
    print(find_greater(value1=input(), value2=input()))


if __name__ == '__main__':
    main()
