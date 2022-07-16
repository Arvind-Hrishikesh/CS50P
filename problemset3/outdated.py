def main():
    month_list=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    x=input("Date: ").lstrip().rstrip()
    try:
        int(x[0])
    except ValueError:
        try:
            month,day_year=x.split(" ",1)
        except ValueError:
            main()
        month=month_list.index(month)+1
        if month<1 or month>12:
            main()
        try:
            day_str,year_str=day_year.split(",")
        except ValueError:
            main()
        day=int(day_str)
        if day<1 or day>31:
                main()
        year=int(year_str)
    else:
        try:
            month_str,day_str,year_str=x.split("/",2)
        except ValueError:
            main()
        month=int(month_str)
        if month<1 or month>12:
                main()
        day=int(day_str)
        if day<1 or day>31:
                main()
        year=int(year_str)
    if day<10 and month<10:
        print(f"{year}-0{month}-0{day}")
    elif day<10 and month>=10:
        print(f"{year}-{month}-0{day}")
    elif day>=10 and month<10:
        print(f"{year}-0{month}-{day}")
    else:
        print(f"{year}-{month}-{day}")


if __name__=="__main__":
    main()