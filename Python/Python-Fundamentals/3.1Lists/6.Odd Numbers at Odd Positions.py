def solve1(lst):
    position = 0
    for number in lst:
        if position % 2 == 1 and number % 2 != 0:
            print(f"Index {position} -> {number}")
        position += 1


# _________________________________________________________________________
# another way
def solve2(lst):
    for number in range(len(lst)):
        if number % 2 == 1 and (lst[number] % 2 != 0):
            print(f"Index {number} -> {lst[number]}")


# _________________________________________________________________________
# another way with enumerate
def solve3(lst):
    for index, number in enumerate(lst):
        if index % 2 == 1 and number % 2 != 0:
            print(f"Index {index} -> {number}")


def main():
    lst = [int(item) for item in input().split(' ')]        # could also be done with map
    solve3(lst)


if __name__ == '__main__':
    main()
