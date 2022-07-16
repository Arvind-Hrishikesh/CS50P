def main():
    x=input("Enter your input here\n")
    convert(x)

def convert(y):
    if ':)' in y:
        y=y.replace(":)","🙂")
    if ':(' in y:
        y=y.replace(":(","🙁")
    print(y)

main()