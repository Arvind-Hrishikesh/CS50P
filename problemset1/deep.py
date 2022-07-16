def main():
    x=input("What is the answer to the Great Question of Life, the Universe and Everything?\n").strip()
    decision(x)

def decision(y):
    if y.lower()=="forty two":
        print("Yes")
    elif y.lower()=="forty-two":
        print("Yes")
    elif y=="42":
        print("Yes")
    else:
        print("No")

main()