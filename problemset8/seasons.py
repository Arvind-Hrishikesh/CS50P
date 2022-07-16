from datetime import date
import sys
import inflect

p=inflect.engine()



def main():
    user_input=input("Date of Birth: ")
    minutes=date_to_minutes(user_input)
    minutes_in_words=num_to_words(minutes)
    print(f"{minutes_in_words}"+" minutes")

def num_to_words(minutes):
    words = p.number_to_words(minutes, andword="").capitalize()
    return words


def date_to_minutes(user_input):
    try:
        year,month,day = user_input.split("-",3)
        date(int(year),int(month),int(day))
    except ValueError:
        sys.exit("Invalid date")
    else:
        current_date = date.today()
        birth_date = date.fromisoformat(user_input)
        return round(((current_date-birth_date).days)*24*60)


if __name__ == "__main__":
    main()