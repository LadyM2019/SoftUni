def main():
    numbers = list(map(int, input().split()))
    numbers.sort(reverse=True)
    n = int(input())
    for times in range(n):
        print(numbers[times], end=" ")


if __name__ == '__main__':
    main()


