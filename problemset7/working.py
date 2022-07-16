import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches=re.search("^([^:]+):*(.*) (AM|PM) to ([^:]+):*(.*) (AM|PM)$",s)
    if matches==None:
        raise ValueError

    in_hour=matches.group(1)
    if matches.group(2)=="":
        in_min="00"
    else:
        in_min=matches.group(2)
    in_AM_PM=matches.group(3)
    out_hour=matches.group(4)
    if matches.group(5)=="":
        out_min="00"
    else:
        out_min=matches.group(5)
    out_AM_PM=matches.group(6)

    if int(in_hour) > 12 or int(out_hour) > 12 or int(in_min) >= 60 or int(out_min) >= 60:
        raise ValueError

    if in_AM_PM=="PM" and in_hour=="12":
        new_in_hour="12"
    elif in_AM_PM=="AM":
        if int(in_hour)<10:
            new_in_hour="0"+in_hour
        elif in_hour=="12":
            new_in_hour="00"
        else:
            new_in_hour=in_hour
    else:
        new_in_hour=str(int(in_hour)+12)

    if out_AM_PM=="PM" and out_hour=="12":
        new_out_hour="12"
    elif out_AM_PM=="AM":
        if int(out_hour)<10:
            new_out_hour="0"+out_hour
        elif out_hour=="12":
            new_out_hour="00"
        else:
            new_out_hour=out_hour
    else:
        new_out_hour=str(int(out_hour)+12)

    return f"{new_in_hour}:{in_min} to {new_out_hour}:{out_min}"



if __name__ == "__main__":
    main()