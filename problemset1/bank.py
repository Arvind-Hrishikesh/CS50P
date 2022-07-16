def main():
    x=input("Enter you greeting\n").strip().lower()
    response(x)

def response(y):
    if y.startswith("hello",0):
        print("$0")
    elif y.startswith("h"):
        print("$20")
    else:
        print("$100")

main()