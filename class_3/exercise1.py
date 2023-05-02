import math ##math.pow(2)


def main():
    list  = [2,9,4,27,81,256]
    for x in range(len(list)):
        print(f"The square of {list[x]} is: {list[x] ** 2}")


if __name__ == "__main__":
    main()