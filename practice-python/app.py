def main():
    i = get_positive()
    print(i)
# testing


def get_positive():
    while True:
        n = int(input("num: "))
        if n > 0:
            break
    return n


if __name__ == "__main__":
    main()
