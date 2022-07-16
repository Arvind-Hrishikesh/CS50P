def main():
    remaining=50
    print(f"Amount Due: {remaining}")

    #Loop starts
    while 1>0:
        coin_input=int(input("Insert Coin: "))
        if coin_input in (25,10,5):
            remaining=remaining-coin_input
        else:
            print(f"Amount Due: {remaining}")
            continue
        if remaining>0:
            print(f"Amount Due: {remaining}")
        else:
            break

    print(f"Change owed: {abs(remaining)}")

if __name__=="__main__":
    main()
