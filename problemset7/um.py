import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches=re.findall("[ ?,\.]+um[ ?,\.]+"," "+s.lower()+" ")
    return len(matches)



if __name__ == "__main__":
    main()