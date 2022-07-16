def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    n=len(plate)

    num_of_letters=0
    if n<=6 and n>=2:
        for l in plate:

            if l in (".",",",";","!","?"," "):
                return False

            try:
                int(l)
            except ValueError:
                num_of_letters+=1
            else:
                break


        if  num_of_letters<n and plate[num_of_letters] == "0":
            return False

        for k in plate[num_of_letters:n]:

            if k in (".",",",";","!","?"," "):
                return False

            try:
                int(k)
            except ValueError:
                return False

    else:
        return False

    if num_of_letters>=2:
            return True


if __name__=="__main__":
    main()