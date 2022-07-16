import random

def main():
    try:
        input_level=int(input("Level: "))
        level=random.randint(1,input_level)
    except ValueError:
        main()
    if level <=0:
        main()
    while 1>0:
        try:
            guess=int(input("Guess: "))
        except ValueError:
            continue
        if guess <=0:
            main()
        elif guess<level:
            print("Too small!")
            continue
        elif guess>level:
            print("Too large!")
            continue
        elif guess==level:
            print("Just right!")
            break

if __name__=="__main__":
    main()


