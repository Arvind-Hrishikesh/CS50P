def main():
    x=input("camel case: ")
    camel_to_snake(x)

def camel_to_snake(y):
    for i in y:
        if i==y[0]:
            snake=i
        elif i.islower():
            snake=snake+i
        elif i.isupper():
            snake=snake+"_"+i.lower()
    print(snake)

main()