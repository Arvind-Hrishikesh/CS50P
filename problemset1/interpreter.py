def main():
    x=input("Enter your mathematical expression here\n")
    decision(x)

def decision(y):
    first_space_index=y.find(" ")
    last_space_index=first_space_index+2
    first_number=y[0:first_space_index]
    operator=y[first_space_index+1]
    last_number=y[(last_space_index+1):(len(y))]

    if operator=="+":
        print(float(int(first_number)+int(last_number)))
    elif operator=="-":
        print(float(int(first_number)-int(last_number)))
    elif operator=="*":
        print(float(int(first_number)*int(last_number)))
    elif operator=="/" and int(last_number)!=0:
        print(round(float(int(first_number)/int(last_number)),2))

main()
