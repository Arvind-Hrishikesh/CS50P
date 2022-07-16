import sys

def main():
    time_input=input("Enter time/n")
    time_now=convert(time_input)
    if 7<=time_now<=8:
        print("breakfast time")
    elif 12<=time_now<=13:
        print("lunch time")
    elif 18<=time_now<=19:
        print("dinner time")
    else:
        pass

def convert(time):
    hours,minutes=time.split(":")
    result=float(int(hours)+float(int(minutes)/60))
    return result

if __name__ == "__main__":
    main()