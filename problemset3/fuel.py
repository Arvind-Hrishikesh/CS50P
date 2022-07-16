def main():
    fuel_input=input("Fraction: ")

    #Checking if there is only one division sign
    div_index=fuel_input.find("/")
    second_div_index=fuel_input.rfind("/")
    if div_index == second_div_index:
        try:
            first_number=int(fuel_input[:div_index])
            second_number=int(fuel_input[div_index+1:])
        except ValueError:
            main()
        else:
            if first_number>second_number:
                main()
            if second_number==0 or second_number<0 or first_number<0:
                main()
            if float((first_number*100)/second_number)<=1:
                print("E")
            elif float((first_number*100)/second_number)>=99:
                print("F")
            else:
                fuel_percent=round((first_number*100)/second_number)
                print(f"{fuel_percent}%")

if __name__=="__main__":
    main()


