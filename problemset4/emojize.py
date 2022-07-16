import emoji

def main():
    x=input("Input: ")
    try:
        find_=x.index("_")
    except ValueError:
        try:
            print(emoji.emojize(x, language='alias'))
        except ValueError:
            main()
    else:
        try:
            print(emoji.emojize(x))
        except ValueError:
            main()

if __name__=="__main__":
    main()