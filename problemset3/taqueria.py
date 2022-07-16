def main():
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    Total=0
    while 1>0:
        try:
            user_input=input("Item: ")
            Total=round(Total+menu[user_input.title()],2)
            txt = "Total: ${price:.2f} dollars!"
            print(txt.format(price = Total))
        except KeyError:
            continue
        except EOFError:
            print()
            break


if __name__=="__main__":
    main()
