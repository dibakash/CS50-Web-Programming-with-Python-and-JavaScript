import sys


def main():
    if len(sys.argv) != 2:
        print("missing command line args")
        sys.exit("1")
    else:
        print("Hello World")
        sys.exit("0")


if __name__ == "__main__":
    main()
