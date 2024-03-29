# Lists inside Dictionary
def create_main_dic():
    dic = dict()
    data = input()

    while data != "end":
        name, numbers = data.split(' -> ')

        if name not in dic:          # only if it is not presented, otherwise it will delete previous values
            dic[name] = []           # if it is NOT initialized it would return a KeyError + name
        try:
            list_numbers = map(int, numbers.split(', '))
            dic[name] += list_numbers
        except ValueError:
            key = numbers
            if key in dic.keys():    # If the other key does not exist, this input line must be IGNORED.
                dic[name] += dic[key]       # dic[key] -> value
        data = input()

    return dic


def main():
    dic = create_main_dic()
    for key, value in dic.items():
        if value:
            print(f"{key} === {', '.join(map(str, value))}")


if __name__ == '__main__':
    main()
