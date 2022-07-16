def main():
    x=input("Input : ")

    for letter in x:
        if letter in ("A","a","E","e","I","i","O","o","U","u"):
            x=x.replace(letter,"")
    print(x)

if __name__=="__main__":
    main()