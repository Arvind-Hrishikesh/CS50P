def main():
    pass

def convert(fuel_input):
    div_index=fuel_input.find("/")
    second_div_index=fuel_input.rfind("/")
    if div_index == second_div_index:

        first_number=int(fuel_input[:div_index])
        second_number=int(fuel_input[div_index+1:])

        if first_number>second_number:
            raise ValueError
        if second_number==0:
            raise ZeroDivisionError
        else:
            fuel_percent=round((first_number*100)/second_number)
            return fuel_percent

def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"

main()