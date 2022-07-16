import random


def main():
    level=get_level()
    score=0
    for i in range(0,10):
        x,y=generate_integer(level)
        for j in range(0,3):
            try:
                print(f"{x} + {y} = ",end="")
                user_input=int(input(""))
            except ValueError:
                if j<2:
                    print("EEE")
                    continue
                elif j==2:
                    print(x+y)
            if user_input==(x+y):
                score+=1
                break
            else:
                if j<2:
                    print("EEE")
                    continue
                elif j==2:
                    print(x+y)
    print(f"Score: {score}")


def get_level():
    level=input("Level: ")
    try:
        [1,2,3].index(int(level))
    except ValueError:
        get_level()
    else:
        return int(level)

def generate_integer(level):
    if level == 1:
        x=random.randint(0,9)
        y=random.randint(0,9)
    elif level == 2:
        x=random.randint(10,99)
        y=random.randint(10,99)
    elif level == 3:
        x=random.randint(100,999)
        y=random.randint(100,999)

    return x,y

if __name__ == "__main__":
    main()