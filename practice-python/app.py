# new python file
import sys


def main():
    if len(sys.argv) != 2:
        print("not 2 args")
        sys.exit(1)
    print(sys.argv)


if __name__ == "__main__":
    main()
