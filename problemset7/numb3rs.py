import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        first,second,third,fourth=ip.split(".")
    except ValueError:
        return False
    else:
        try:
            int(first)
            int(second)
            int(third)
            int(fourth)
        except ValueError:
            return False
        else:
            if 0<=int(first)<=255 and 0<=int(second)<=255 and 0<=int(third)<=255 and 0<=int(fourth)<=255:
                return True
            else:
                return False


if __name__ == "__main__":
    main()