import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches=re.search("(https?.+youtu)(be)+\.com/embed(.+)\".+",s)
    if matches==None:
        return matches
    elif matches.group(1):
        return "https://youtu."+matches.group(2)+matches.group(3)



if __name__ == "__main__":
    main()